from django.shortcuts import render
from django.http import HttpResponse
import subprocess

def test_view(request):
    return render(request, 'mytest/test.html',{})




def open_folder(request, folder_path):
    try:
        # Use the 'explorer' command on Windows to open the folder
        subprocess.Popen(['explorer', folder_path], shell=True)
        return HttpResponse("Folder opened successfully.")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")