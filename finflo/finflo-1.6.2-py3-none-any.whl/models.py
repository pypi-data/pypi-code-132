from ast import excepthandler
from xml.dom import ValidationErr
from django.db import models
from .middleware import get_current_user
from .validators import validate_postive
from django.core.exceptions import ValidationError



try:
   from django.conf import settings
except ImportError:
    raise Exception("settings.py file is required to run this project")



## CORE CONFIGURATIONS CLASSES ##


class Temp(models.Model):
    pass


class Flowmodel(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "1. FlowModel"


# Create your models here.

class TransitionManager(models.Model):
    t_id = models.IntegerField()
    type = models.CharField(max_length = 255 )
    sub_sign = models.IntegerField(default = 0 )

    # default 1 for initial submit and maker process

    def save(self, *args, **kwargs):
        self.type = self.type.upper()
        return super(TransitionManager,self).save(*args, **kwargs)
    
    def __str__(self):
        return "{0}_{1}".format(self.type.lower() , self.id)


class SignList(models.Model):
    sign_id = models.IntegerField()
    name = models.CharField(max_length = 255 , default = None)
    sub_name = models.CharField(max_length = 255 , default = None)

    def __str__(self):
        return self.name
    

class States(models.Model):
    description = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "2. States"

    def __str__(self):
        return self.description


class Action(models.Model):
    description = models.CharField(max_length=255 , blank = True , null=True , help_text = 'e.g., SUBMIT , DELETE') 
    model = models.ForeignKey(Flowmodel , on_delete = models.CASCADE , blank = True , null = True )
    from_state = models.ForeignKey(States , on_delete= models.DO_NOTHING , related_name = 'action_from_state' , blank = True , null = True , help_text = "initial from state for transition ")
    to_state = models.ForeignKey(States , on_delete= models.DO_NOTHING , blank = True , null = True , help_text = "final state for the transition to take place")
    # optional fields
    intermediator = models.BooleanField(default = False)
    from_party = models.ForeignKey(settings.FINFLO['FROM_PARTY'] or Temp , models.SET_NULL , blank = True , null = True , help_text = 'this field is optional' , related_name = 'from_transition_party')
    to_party = models.ForeignKey(settings.FINFLO['TO_PARTY'] or Temp , models.SET_NULL , blank = True , null = True , help_text = 'this field is optional' , related_name = 'to_last_party')
    stage_required = models.ForeignKey(SignList , on_delete= models.DO_NOTHING ,blank = True , null = True ,help_text = "IMPORTANT : if 0 means initial_transition ")
    
    def save(self, *args, **kwargs):
        self.description = self.description.upper()
        # try:
        #     sign_len = SignList.objects.get(name = self.stage_required )
        #     self.sign_required = sign_len.sign_id
        # except:
        #     pass
        return super(Action,self).save(*args, **kwargs)

    def __str__(self):
        return "{0} -> {1}".format(self.description , self.model)

    class Meta:
        verbose_name_plural = "3. Action"
        unique_together = ('description', 'model') 
 

class workflowitems(models.Model):
    
    created_date = models.DateTimeField(auto_now_add=True)
    transitionmanager = models.OneToOneField(TransitionManager, on_delete=models.CASCADE,blank=True, null=True )
    initial_state  = models.CharField(max_length=50,default = 'DRAFT')
    interim_state = models.CharField(max_length=50,default = 'DRAFT')
    final_state = models.CharField(max_length=50,default = 'DRAFT') 
    event_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING , blank=True, null=True)
    next_available_transitions =  models.CharField(max_length=500)
    current_from_party = models.ForeignKey(settings.FINFLO['FROM_PARTY'] or Temp , models.SET_NULL , blank = True , null = True , editable = False , related_name = 'wf_from_party')
    current_to_party = models.ForeignKey(settings.FINFLO['TO_PARTY'] or Temp , models.SET_NULL , blank = True , null = True , editable = False )
    action = models.CharField(max_length=25 , blank=True, null=True , default = 'DRAFT')
    subaction = models.CharField(max_length=55 , blank=True, null=True)
    previous_action = models.CharField(max_length=55 , blank=True, null=True)
    model_type  = models.CharField(max_length=55, blank=True, null=True)
    comments = models.CharField(max_length=500,blank=True, null=True)
    is_read = models.BooleanField(default=True,blank=True, null=True)
    final_value = models.BooleanField(default=False,blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "WorkFlowItem"
        ordering = ['id']

    # def save(self, *args, **kwargs):
    #    if self.from_party is None:
    #         self.from_party = None
    #    super(workflowitems, self).save(*args, **kwargs) # Call the real save() method


# WORKEVENTS
class workevents(models.Model):

    workflowitems = models.ForeignKey(workflowitems, on_delete=models.CASCADE , related_name='WorkFlowEvents')
    action = models.CharField(max_length=25, blank=True, null=True , default = 'DRAFT')
    subaction = models.CharField(max_length=55 , blank=True, null=True , default = 'DRAFT')
    initial_state  = models.CharField(max_length=50 , default = 'DRAFT')
    interim_state = models.CharField(max_length=50,default = 'DRAFT')
    final_state = models.CharField(max_length=50,default = 'DRAFT')
    from_party = models.ForeignKey(settings.FINFLO['FROM_PARTY'] or Temp , models.SET_NULL , blank = True , null = True , editable = False ,related_name = 'we_from_party')
    to_party = models.ForeignKey(settings.FINFLO['TO_PARTY'] or Temp , models.SET_NULL , blank = True , null = True , editable = False )
    event_user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.DO_NOTHING , blank=True, null=True)
    is_read = models.BooleanField(default=True,blank=True, null=True)
    final_value = models.BooleanField(default=False,blank=True, null=True)
    comments = models.CharField(max_length=500,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=55, blank=True, null=True)
    

    class Meta:
        verbose_name_plural = "WorkFlowEvent"
        ordering = ['id']





