# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey('UsersCustomuser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class FilesRepository(models.Model):
    associated_conflux_id = models.IntegerField()
    file_origin_type = models.CharField(max_length=100, blank=True, null=True)
    document = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files_repository'


class IndxxAssignedProcess(models.Model):
    code = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    target_in_hours = models.IntegerField(blank=True, null=True)
    dept = models.ForeignKey('IndxxDept', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'indxx_assigned_process'


class IndxxAssignedTask(models.Model):
    task_assignee = models.CharField(max_length=100, blank=True, null=True)
    was_linked_with = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField()
    snoonze_me = models.CharField(max_length=10, blank=True, null=True)
    task_desnoozed_at = models.DateTimeField(blank=True, null=True)
    snooze_desc = models.CharField(max_length=100, blank=True, null=True)
    sla_breached_flag = models.BooleanField(blank=True, null=True)
    days_for_sla_mail_sent = models.IntegerField(blank=True, null=True)
    complete_by = models.DateTimeField(blank=True, null=True)
    assigned_author = models.ForeignKey('IndxxAuthor', models.DO_NOTHING, blank=True, null=True)
    assigned_process = models.ForeignKey(IndxxAssignedProcess, models.DO_NOTHING)
    assigned_status = models.ForeignKey('IndxxAssignedTaskStatus', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'indxx_assigned_task'


class IndxxAssignedTaskStatus(models.Model):
    status_code = models.CharField(max_length=1000)
    status_desc = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'indxx_assigned_task_status'


class IndxxAuthor(models.Model):
    author_desc = models.CharField(max_length=1000, blank=True, null=True)
    conflux = models.IntegerField(blank=True, null=True)
    is_maker_instance = models.BooleanField()
    author_assignee = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField()
    sla_breached_flag = models.BooleanField(blank=True, null=True)
    days_for_sla_mail_sent = models.IntegerField(blank=True, null=True)
    was_rejected = models.BooleanField(blank=True, null=True)
    author_status = models.ForeignKey('IndxxAuthorStatus', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'indxx_author'


class IndxxAuthorStatus(models.Model):
    status_code = models.CharField(max_length=1000)
    status_desc = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'indxx_author_status'


class IndxxBlock(models.Model):
    code = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    next_approved = models.CharField(max_length=1000, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    first = models.BooleanField()
    last = models.BooleanField()
    target_in_hours = models.IntegerField(blank=True, null=True)
    steps_to_goback = models.IntegerField()
    assigned_process = models.ForeignKey(IndxxAssignedProcess, models.DO_NOTHING, blank=True, null=True)
    process = models.ForeignKey('IndxxProcess', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'indxx_block'


class IndxxConfluxid(models.Model):
    latest_value = models.IntegerField()
    created_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'indxx_confluxid'


class IndxxDept(models.Model):
    name = models.CharField(max_length=1000)
    code = models.CharField(max_length=1000, blank=True, null=True)
    short_name = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'indxx_dept'


class IndxxMaker(models.Model):
    created_on = models.DateTimeField()
    approver = models.CharField(max_length=1000, blank=True, null=True)
    confluxid = models.IntegerField()
    maker_assignee = models.CharField(max_length=100, blank=True, null=True)
    maker_description = models.CharField(max_length=100, blank=True, null=True)
    snoonze_me = models.CharField(max_length=10, blank=True, null=True)
    process_desnoozed_at = models.DateTimeField(blank=True, null=True)
    snooze_desc = models.CharField(max_length=100, blank=True, null=True)
    sla_breached_flag = models.BooleanField(blank=True, null=True)
    days_for_sla_mail_sent = models.IntegerField(blank=True, null=True)
    complete_by = models.DateTimeField(blank=True, null=True)
    block = models.ForeignKey(IndxxBlock, models.DO_NOTHING)
    linked_task = models.ForeignKey(IndxxAssignedTask, models.DO_NOTHING, blank=True, null=True)
    maker_author = models.ForeignKey(IndxxAuthor, models.DO_NOTHING, blank=True, null=True)
    maker_status = models.ForeignKey('IndxxMakerStatus', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'indxx_maker'


class IndxxMakerStatus(models.Model):
    status_code = models.CharField(max_length=1000)
    status_desc = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'indxx_maker_status'


class IndxxProcess(models.Model):
    name = models.CharField(max_length=1000)
    code = models.CharField(max_length=1000, blank=True, null=True)
    target_process = models.IntegerField(blank=True, null=True)
    dept = models.ForeignKey(IndxxDept, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indxx_process'


class IndxxRejectReasons(models.Model):
    task_identified_by = models.IntegerField(blank=True, null=True)
    is_maker_instance = models.BooleanField(blank=True, null=True)
    assigned_process_rejected_at = models.ForeignKey(IndxxAssignedProcess, models.DO_NOTHING, blank=True, null=True)
    block_id_rejected_at = models.ForeignKey(IndxxBlock, models.DO_NOTHING, blank=True, null=True)
    rejected_by = models.ForeignKey(IndxxAuthor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indxx_reject_reasons'


class IndxxUserdeptassosciation(models.Model):
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    can_be_approver = models.BooleanField()
    department = models.ForeignKey(IndxxDept, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'indxx_userdeptassosciation'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class UsersCustomuser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    email = models.CharField(unique=True, max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_customuser'


class UsersCustomuserGroups(models.Model):
    customuser = models.ForeignKey(UsersCustomuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_customuser_groups'
        unique_together = (('customuser', 'group'),)


class UsersCustomuserUserPermissions(models.Model):
    customuser = models.ForeignKey(UsersCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)
