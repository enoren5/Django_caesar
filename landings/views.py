from django.shortcuts import render
import string

def caesar(request):
    # Courtesy of Real Python: https://realpython.com/python-practice-problems/
    plain_text = request.GET['original_entry']
    shift_num = request.GET['shift_num']
    shift_num = int(shift_num)
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters, mask)
    output_text = plain_text.translate(trantab)
    context = {'output_text': output_text, 'original_entry': plain_text,}
    return render(request, 'landings/home.html', context)


# print(caesar("abcdefghijklmnopqrstuvwxyz", 3))
# Create your views here.

# def home(request):    
# return render(request, 'landings/home.html')