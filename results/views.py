from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Results
from .serializers import ResultsSerializer
from .permissions import ResultUserOnly, ResultUserReadDeleteOrAdminUpdate


class ResultsList(ListAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = [IsAdminUser]


class UserResults(ListAPIView):
    serializer_class = ResultsSerializer
    permission_classes = [ResultUserOnly]

    def get_queryset(self):
        result_user = self.request.user
        return Results.objects.filter(result_user=result_user)


class ResultDetails(RetrieveUpdateDestroyAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = [ResultUserReadDeleteOrAdminUpdate]


class ResultCreate(CreateAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        result_user = self.request.user
        serializer.save(result_user=result_user)




