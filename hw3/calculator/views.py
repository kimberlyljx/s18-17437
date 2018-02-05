# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import math

INT_MAX = 1000000
INT_MIN = -1000000

def reset_context(context):
    context['new_value'] = str(0)
    context['prev_value'] = str(0)
    context['prev_op'] = '+'
    context['last_was_op'] = str(False)
    context['display'] = str(0)

def is_valid_op(op_string):
    return (op_string == '+' or op_string == '-' or op_string == '*' or 
            op_string == '/' or op_string == '=') 

def is_valid_digit(digit_str):
    try:
        int_val = int(digit_str)
        return not (math.isnan(int_val) or 
                    int_val > INT_MAX or 
                    int_val < INT_MIN)
    except:
        return False

def is_valid_eval(request):
    if ('prev_op' not in request.POST or
        'new_value' not in request.POST or
        'prev_value' not in request.POST):
        return False
    else:
        return (is_valid_op(request.POST['prev_op']) and 
                is_valid_digit(request.POST['prev_value']) and
                is_valid_digit(request.POST['new_value']))

def evaluate(request, context):
    res = True
    if (is_valid_eval(request)):
        prev_value = int(request.POST['prev_value'])
        new_value = int(request.POST['new_value'])
        if (request.POST['prev_op'] == '+'):
            context['prev_value'] = str(new_value + prev_value)
        elif (request.POST['prev_op'] == '-'):
            context['prev_value'] = str(prev_value - new_value)
        elif (request.POST['prev_op'] == '*'):
            context['prev_value'] = str(prev_value * new_value)
        elif (request.POST['prev_op'] == '/' and new_value != 0):
            context['prev_value'] = str(int(math.floor(prev_value / new_value)))
        else:
            res = False
    else:
        res = False
    return res

def str_to_bool(s):
    if s == 'True':
        return True
    elif s == 'False':
        return False
    else:
        raise ValueError

def attrs_exist(request):
    return ('new_value' in request.POST and
        'prev_value' in request.POST and
        'prev_op' in request.POST and
        'last_was_op' in request.POST and
        'display' in request.POST)

def digit_press(request, context):
    try:
        digit = int(request.POST['digit'])
        new_value = int(request.POST['new_value'])
        context['prev_value'] = request.POST['prev_value']
        new_value = new_value * 10 + digit
        context['new_value'] = str(new_value)
        context['display'] = str(new_value)
        context['last_was_op'] = str(False)   
        context['prev_op'] = request.POST['prev_op']         
        return render(request, 'calculator/calculator.html', context)
    except:
        reset_context(context)
        context['errors'] = "Invalid digit"
        return render(request, 'calculator/calculator.html', context)

def operator_press(request, context):
    try:
        if (str_to_bool(request.POST['last_was_op'])):
            context['display'] = request.POST['display']
            context['new_value'] = request.POST['new_value']
            context['prev_value'] = request.POST['prev_value']
            context['prev_op'] = request.POST['operator']
            context['last_was_op'] = str(True)
            return render(request, 'calculator/calculator.html', context)
        else:
            if (evaluate(request, context)):
                res = context['prev_value']
                context['display'] = context['prev_value']
                context['prev_op'] = request.POST['operator']
                context['new_value'] = str(0)
                context['last_was_op'] = str(True)
                if (request.POST['operator'] == '='):
                    reset_context(context);
                    context['display'] = res
                    return render(request, 'calculator/calculator.html', context)
                return render(request, 'calculator/calculator.html', context)                    
            else:
                reset_context(context)
                context['errors']  = 'Invalid evaluation'                   
                return render(request, 'calculator/calculator.html', context)
    except:
        reset_context(context)
        context['errors']  = 'Invalid parameters'                           
        return render(request, 'calculator/calculator.html', context)

# Create your views here.
def home_page(request):
    # render takes: (1) the request,
    #               (2) the name of the view to generate, and
    #               (3) a dictionary of name-value pairs of data to be
    #                   available to the view.
    # return render(request, 'calculator/calculator.html', {})

    context = {}

    if not attrs_exist(request):
        reset_context(context)
        context['errors'] = "Fresh Calculator"
        return render(request, 'calculator/calculator.html', context)

    if 'digit' in request.POST:
        return digit_press(request, context)
        
    if 'operator' in request.POST and is_valid_op(request.POST['operator']):
        return operator_press(request, context)

    reset_context(context)
    return render(request, 'calculator/calculator.html', context)

