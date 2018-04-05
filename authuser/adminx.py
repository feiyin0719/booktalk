import xadmin
from django.contrib import admin

# Register your models here.
from xadmin.layout import Main, Fieldset, Row, Side
from xadmin.plugins.auth import PermissionModelMultipleChoiceField, UserAdmin
from django.utils.translation import ugettext_lazy as _
from authuser.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from authuser.models import MyUser
from authuser.views import MyChangePasswordView


class MyUserAdmin(UserAdmin):
    reversion_enable=True
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','mobile',
                    'profile','headimg','enable')
    #list_editable=['is_staff',]
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    style_fields = {'user_permissions': 'm2m_transfer'}
    model_icon = 'fa fa-user'
    relfield_style = 'fk-ajax'
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    def get_model_form(self, **kwargs):
        if self.org_obj is None:
            self.form = UserCreationForm
        else:
            self.form = UserChangeForm
        return super(UserAdmin, self).get_model_form(**kwargs)
    def get_readonly_fields(self):
        if self.request.user.is_superuser:
            readonly_fields=()
        else:
            readonly_fields=('username','is_staff','is_active','date_joined','is_superuser','groups','user_permissions','enable','last_login')
        return readonly_fields
    def get_field_attrs(self, db_field, **kwargs):
        attrs = super(UserAdmin, self).get_field_attrs(db_field, **kwargs)
        if db_field.name == 'user_permissions':
            attrs['form_class'] = PermissionModelMultipleChoiceField
        return attrs
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('first_name', 'last_name'),
                             Row('email','mobile'),
                             'headImage','profile',
                             'zhifubao'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_superuser'
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()
    def queryset(self):
        q=self.model._default_manager.get_queryset()
        if not self.request.user.is_superuser:
            q=q.filter(id=self.request.user.id)
        return q
xadmin.site.unregister(MyUser)
xadmin.site.register(MyUser, MyUserAdmin)
xadmin.site.register_view(r'^myuser/myuser/(.+)/update/password/$',
                   MyChangePasswordView, name='user_change_password')
# xadmin.site.register_view(r'^eshopadmin/myuser/(.+)/update/password/$',
#                    MyChangePasswordView, name='user_change_password')
