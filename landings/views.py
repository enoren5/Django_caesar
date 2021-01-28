from django.shortcuts import render
import string

def caesar(request):
    # Courtesy of Real Python: https://realpython.com/python-practice-problems/
    if 'encrypt' in request.GET:
        plain_text = request.GET['original_entry']
        shift_num = request.GET['shift_num']
        shift_num = int(shift_num)
        letters = string.ascii_lowercase
        mask = letters[shift_num:] + letters[:shift_num]
        trantab = str.maketrans(letters, mask)
        output_text = plain_text.translate(trantab)
        context = {'select_option': False, 'output_text': output_text, 'original_entry': plain_text, 'conv_decrypt': False, 'conv_encrypt': True}
        return render(request, 'landings/home.html', context)
    
    elif 'decrypt' in request.GET:
        plain_text = request.GET['original_entry']
        shift_num = request.GET['shift_num']
        shift_num = -int(shift_num)
        letters = string.ascii_lowercase
        mask = letters[shift_num:] + letters[:shift_num]
        trantab = str.maketrans(letters, mask)
        output_text = plain_text.translate(trantab)
        context = {'select_option': False, 'output_text': output_text, 'original_entry': plain_text, 'conv_decrypt': True, 'conv_encrypt': False}
        return render(request, 'landings/home.html', context)
    
    elif 'conversion' in request.GET:
        conversion = request.GET['conversion']
        if conversion == 'encrypt':
            context = {'select_option': False, 'result_encrypt': True, 'result_decrypt': False, 'conv_decrypt': True, 'conv_encrypt': False, 'conv_decrypt': False, 'conv_encrypt': True}
            return render(request, 'landings/home.html', context)
        elif conversion == 'decrypt':
            context = {'select_option': False, 'result_encrypt': False, 'result_decrypt': True}
            return render(request, 'landings/home.html', context)
    
    return render(request, 'landings/home.html')

# print(caesar("abcdefghijklmnopqrstuvwxyz", 3))
# Create your views here.

# def home(request):    
# return render(request, 'landings/home.html')