from crispy_forms.helper import FormHelper
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.utils.html import escape
from django.views.decorators.debug import sensitive_post_parameters
from xadmin.util import unquote
from xadmin.views import ModelAdminView, csrf_protect_m
from django.utils.translation import ugettext_lazy as _
from authuser.forms import AdminPasswordChangeForm
from authuser.models import MyUser


class MyChangePasswordView(ModelAdminView):
    model =MyUser
    change_password_form = AdminPasswordChangeForm
    change_user_password_template = None

    @csrf_protect_m
    def get(self, request, object_id):
        if not self.has_change_permission(request):
            raise PermissionDenied
        self.obj = self.get_object(unquote(object_id))
        self.form = self.change_password_form(self.obj)

        return self.get_response()

    def get_media(self):
        media = super(MyChangePasswordView, self).get_media()
        media = media + self.vendor('xadmin.form.css', 'xadmin.page.form.js') + self.form.media
        return media

    def get_context(self):
        context = super(MyChangePasswordView, self).get_context()
        helper = FormHelper()
        helper.form_tag = False
        self.form.helper = helper
        context.update({
            'title': _('Change password: %s') % escape(unicode(self.obj)),
            'form': self.form,
            'has_delete_permission': False,
            'has_change_permission': True,
            'has_view_permission': True,
            'original': self.obj,
        })
        return context

    def get_response(self):
        return TemplateResponse(self.request, [
            self.change_user_password_template or
            'xadmin/auth/user/change_password.html'
        ], self.get_context(), current_app=self.admin_site.name)

    @method_decorator(sensitive_post_parameters())
    @csrf_protect_m
    def post(self, request, object_id):
        if not self.has_change_permission(request):
            raise PermissionDenied
        self.obj = self.get_object(unquote(object_id))
        self.form = self.change_password_form(self.obj, request.POST)

        if self.form.is_valid():
            self.form.save()
            self.message_user(_('Password changed successfully.'), 'success')
            return HttpResponseRedirect(self.model_admin_url('change', self.obj.pk))
        else:
            return self.get_response()