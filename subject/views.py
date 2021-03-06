from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from subject.models import Subject
from rest_framework.response import Response
from subject.serializers import SubjectSerializer


# Create subject RestAPI views to use in frontand.
class SubjectViews(APIView):
    """
    List all subject, or create a new subject.
    """

    def get(self, request, format=None):
        try:
            subjects = Subject.objects.all()
            serializer = SubjectSerializer(subjects, many=True)
            # print(len(serializer.data))
            if len(serializer.data) > 0:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(data="subjects not found :(", status=status.HTTP_404_NOT_FOUND)
        except subjects.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# subject details also for update and destroy
class SubjectDetailsViews(APIView):
    """Single subject all method"""

    def get_subjects(self, pk):
        try:
            tec = Subject.objects.get(pk=pk)
            return tec
        except Subject.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # print(pk)
        subject = self.get_subjects(pk)
        return Response(subject, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        subject = self.get_subjects(pk)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_426_UPGRADE_REQUIRED)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subject = self.get_subjects(pk)
        if subject:
            subject.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
