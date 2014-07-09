from django.db import models

class Role(models.Model):
    rid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    class Meta:
        db_table = 'role'

class Users(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=60)
    pass_field = models.CharField(db_column='pass', max_length=32) # Field renamed because it was a Python reserved word.
    mail = models.CharField(max_length=64, blank=True)
    mode = models.IntegerField()
    sort = models.IntegerField(blank=True, null=True)
    threshold = models.IntegerField(blank=True, null=True)
    theme = models.CharField(max_length=255)
    signature = models.CharField(max_length=255)
    signature_format = models.IntegerField()
    created = models.IntegerField()
    access = models.IntegerField()
    login = models.IntegerField()
    status = models.IntegerField()
    timezone = models.CharField(max_length=8, blank=True)
    language = models.CharField(max_length=12)
    picture = models.CharField(max_length=255)
    init = models.CharField(max_length=64, blank=True)
    data = models.TextField(blank=True)
    last_login = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'users'

class UsersRoles(models.Model):
    uid = models.ForeignKey(Users, db_column='uid')
    rid = models.ForeignKey(Role, db_column='rid')
    class Meta:
        db_table = 'users_roles'

class FossCategories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    workshop = models.IntegerField()
    foss_desc = models.TextField()
    class Meta:
        db_table = 'foss_categories'

class TutorialLanguages(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    class Meta:
        db_table = 'tutorial_languages'

class TutorialDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    foss_category = models.CharField(max_length=255)
    tutorial_name = models.CharField(max_length=600)
    tutorial_level = models.CharField(max_length=400)
    order_code = models.IntegerField()
    class Meta:
        db_table = 'tutorial_details'

class TutorialCommonContents(models.Model):
    id = models.IntegerField(primary_key=True)
    tutorial_detail = models.ForeignKey(TutorialDetails)
    tutorial_slide = models.TextField()
    tutorial_slide_uid = models.ForeignKey(Users, related_name='slides', db_column='tutorial_slide_uid')
    tutorial_slide_status = models.IntegerField()
    tutorial_code = models.TextField()
    tutorial_code_uid = models.ForeignKey(Users, related_name='codes', db_column='tutorial_code_uid')
    tutorial_code_status = models.IntegerField()
    tutorial_assignment = models.TextField()
    tutorial_assignment_uid = models.ForeignKey(Users, related_name='assignments', db_column='tutorial_assignment_uid')
    tutorial_assignment_status = models.IntegerField()
    tutorial_prerequisit = models.IntegerField()
    tutorial_prerequisit_uid = models.ForeignKey(Users, related_name='prerequisite', db_column='tutorial_prerequisit_uid')
    tutorial_prerequisit_status = models.IntegerField()
    tutorial_keywords = models.TextField()
    tutorial_keywords_uid = models.ForeignKey(Users, related_name='keywords', db_column='tutorial_keywords_uid')
    class Meta:
        db_table = 'tutorial_common_contents'

class TutorialResources(models.Model):
    id = models.IntegerField(primary_key=True)
    tutorial_detail = models.ForeignKey(TutorialDetails)
    uid = models.ForeignKey(Users, db_column='uid')
    language = models.CharField(max_length=50)
    upload_time = models.DateTimeField()
    reviewer = models.CharField(max_length=400)
    tutorial_content = models.ForeignKey(TutorialCommonContents)
    tutorial_outline = models.TextField()
    tutorial_outline_uid = models.ForeignKey(Users, related_name='outlines', db_column='tutorial_outline_uid')
    tutorial_outline_status = models.IntegerField()
    tutorial_script = models.TextField()
    tutorial_script_uid = models.ForeignKey(Users, related_name='scripts', db_column='tutorial_script_uid')
    tutorial_script_status = models.IntegerField()
    tutorial_script_timed = models.TextField()
    tutorial_video = models.TextField()
    tutorial_video_uid = models.ForeignKey(Users, related_name='videos', db_column='tutorial_video_uid')
    tutorial_video_status = models.IntegerField()
    tutorial_status = models.CharField(max_length=50)
    cvideo_version = models.IntegerField()
    hit_count = models.BigIntegerField()
    request_exception = models.TextField()
    class Meta:
        db_table = 'tutorial_resources'

class TutorialDomainReviewerRoles(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.ForeignKey(Users, db_column='uid')
    language = models.ForeignKey(TutorialLanguages)
    class Meta:
        db_table = 'tutorial_domain_reviewer_roles'

class TutorialQualityRoles(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.ForeignKey(Users, db_column='uid')
    language = models.ForeignKey(TutorialLanguages)
    class Meta:
        db_table = 'tutorial_quality_roles'

class TutorialUpdateLog(models.Model):
    id = models.IntegerField(primary_key=True)
    tutorial_resources = models.ForeignKey(TutorialResources)
    update_time = models.DateTimeField()
    updated_by = models.CharField(max_length=255)
    updated_content = models.CharField(max_length=255)
    class Meta:
        db_table = 'tutorial_update_log'

class TutorialMissingComponent(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.ForeignKey(Users, db_column='uid')
    trid = models.ForeignKey(TutorialResources, db_column='trid')
    component = models.CharField(max_length=15)
    type = models.IntegerField()
    remarks = models.TextField()
    reported = models.IntegerField()
    reply_status = models.IntegerField()
    created = models.DateField()
    updated = models.DateField()
    email = models.CharField(max_length=100)
    class Meta:
        db_table = 'tutorial_missing_component'

class TutorialMissingComponentReply(models.Model):
    id = models.IntegerField(primary_key=True)
    missing_component_id = models.IntegerField()
    uid = models.ForeignKey(Users, db_column='uid')
    reply_message = models.TextField()
    created = models.DateTimeField()
    class Meta:
        db_table = 'tutorial_missing_component_reply'

class TutorialPublicReview(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.ForeignKey(Users, db_column='uid')
    trid = models.ForeignKey(TutorialResources, db_column='trid')
    date_time = models.DateTimeField()
    component = models.CharField(max_length=20)
    comment = models.TextField()
    class Meta:
        db_table = 'tutorial_public_review'

class TutorialPublicReviewVideo(models.Model):
    id = models.IntegerField(primary_key=True)
    tutorial_public_review = models.ForeignKey(TutorialPublicReview)
    item = models.IntegerField()
    everywhere = models.IntegerField()
    video_time = models.TimeField()
    class Meta:
        db_table = 'tutorial_public_review_video'

class UserRatings(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.ForeignKey(Users, db_column='uid')
    page_id = models.IntegerField()
    rated_date = models.DateField()
    rating = models.BigIntegerField()
    class Meta:
        db_table = 'user_ratings'

class VideoComments(models.Model):
    id = models.IntegerField(primary_key=True)
    tutorial_resource = models.ForeignKey(TutorialResources)
    uid = models.ForeignKey(Users, db_column='uid')
    comments = models.TextField()
    created_at = models.DateTimeField()
    class Meta:
        db_table = 'video_comments'