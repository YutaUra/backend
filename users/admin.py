from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from users.models import User, Profile, FollowRelation


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', "pub_id")


class ProfileInline(admin.StackedInline):
    model = Profile
    max_num = 1
    can_delete = False


class FollowInline(admin.StackedInline):
    model = FollowRelation
    fk_name = 'user'


class FollowerInline(admin.StackedInline):
    model = FollowRelation
    fk_name = 'follow_user'


class MyUserAdmin(UserAdmin):
    inlines = [
        ProfileInline,
        FollowInline,
        FollowerInline,
    ]
    fieldsets = (
        (None, {'fields': ('email', 'pub_id', 'password')}),
        (_('Personal info'), {'fields': ("_position",)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', "_position", 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', "_position",)
    ordering = ('email',)


admin.site.register(User, MyUserAdmin)
