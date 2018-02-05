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

def is_valid_eval(context):
    if (context['prev_op'] not in request.POST or
        context['new_value'] not in request.POST or
        context['prev_value'] not in request.POST):
        return False
    else:
        return (is_valid_op(context['prev_op']) and 
                is_valid_digit(context['prev_value']) and
                is_valid_digit(context['new_value']))

def evaluate(context):
    res = True
    if (is_valid_eval(context)):
        prev_value = int(context['prev_value'])
        new_value = int(context['new_value'])
        if (context['prev_op'] == '+'):
            prev_value = new_value + prev_value;
        elif (context['prev_op'] == '-'):
            prev_value = prev_value - new_value;
        elif (context['prev_op'] == '*'):
            prev_value = prev_value * new_value;
        elif (context['prev_op'] == '/' and new_value != 0):
            prev_value = Math.floor(prev_value / new_value)
        else:
            reset_context(context)
            res = False
    else:
        reset_context(context)
        res = False
    return res

# Create your views here.
def home_page(request):
    # render takes: (1) the request,
    #               (2) the name of the view to generate, and
    #               (3) a dictionary of name-value pairs of data to be
    #                   available to the view.
    # return render(request, 'calculator/calculator.html', {})

    context = {}

    if 'reset' in request.POST:
        print("hit")

        reset_context(context)
        return render(request, 'calculator/calculator.html', context)
    
    if 'digit' in request.POST:
        print("digit")
        digit = 0
        try:
            digit = int(request.POST['digit'])
            new_value = int(request.POST['new_value'])
            new_value = new_value * 10 + digit
            context['new_value'] = str(new_value)
            context['display'] = str(new_value)
            context['last_was_op'] = str(False)            
            return render(request, 'calculator/calculator.html', context)
        except:
            reset_context(context)
            return render(request, 'calculator/calculator.html', context)
        
    if 'operator' in request.POST and is_valid_op(context['operator']):
        print("operator")

        try:
            if (bool(context['last_was_op'])):
                context['prev_op'] = context['operator']
                return render(request, 'calculator/calculator.html', context)
            else:
                if (evaluate(context)):
                    context['display'] = context['prev_value']
                    context['prev_op'] = context['operator']
                    context['new_value'] = str(0)
                    context['last_was_op'] = str(True)
                    if (context['operator'] == '='):
                        reset_context();
                        context['display'] = context['prev_value']
                        return render(request, 'calculator/calculator.html', context)
                else:
                    return render(request, 'calculator/calculator.html', context)
        except:
            reset_context(context)
            return render(request, 'calculator/calculator.html', context)

    print("reset")

    reset_context(context)
    return render(request, 'calculator/calculator.html', context)

