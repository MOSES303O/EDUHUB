# EDUHUB
 THIS IS  A  DJANGO COURSE MAPPER PROJECT.

"""
class Courses(models.Model):
    id = models.UUIDField(editable=False,default=uuid.uuid4, primary_key=True)
    universityList=models.ForeignKey(UniversityList,on_delete=models.CASCADE,related_name='course')
    name = models.CharField(max_length=200)
    coursecode=models.PositiveIntegerField(default=0,unique=True)
    details=models.OneToOneField(CourseDetail,on_delete=models.SET_NULL,null=True,blank=True)
    class Meta:
        ordering=['name']    
        unique_together=('universityList','name')

class CourseRequirement(models.Model):
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    subjects=models.TextField()
    cluster_wights21=models.DecimalField(max_digits=5,decimal_places=3)
    cluster_wights22=models.DecimalField(max_digits=5,decimal_places=3)
    #details=models.TextField(default='tttt') 

"""   