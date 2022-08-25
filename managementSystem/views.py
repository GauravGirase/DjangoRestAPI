from rest_framework import viewsets
from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer



class SchoolViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing School instances.
    """
    serializer_class = SchoolSerializer
    queryset = School.objects.all()

    def get_serializer_context(self):
        context = super(SchoolViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context


class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Student instances.
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get_serializer_context(self):
        context = super(StudentViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context
