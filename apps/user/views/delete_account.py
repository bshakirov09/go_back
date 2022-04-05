from rest_framework.views import APIView, Response


class DeleteAccountView(APIView):

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({'detail': 'successfully'})
