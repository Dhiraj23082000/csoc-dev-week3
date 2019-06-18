from django.shortcuts import render
from django.shortcuts import get_object_or_404
from store.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.

def index(request):
    return render(request, 'store/index.html')

def bookDetailView(request, bid):
    template_name='store/book_detail.html'
    context={
           'book' :None,
           'num_available':None,

         }


    tg = Book.objects.get(id=bid)
    context['book']= tg
    try:
        present = BookCopy.objects.get(book = tg)
        context['num_available']=0
    except:
        context['num_available']=1

    # START YOUR CODE HERE


    return render(request,template_name, context=context)


def bookListView(request):
    template_name='store/book_list.html'

    get_data=request.GET
    # START YOUR CODE HERE
    let = Book.objects.all().order_by('mrp')
    context={
    'books':let, # set here the list of required books upon filtering using the GET parameters
    }

    return render(request,template_name, context=context)

@login_required
def viewLoanedBooks(request):
    template_name='store/loaned_books.html'
    lemda = BookCopy.objects.filter(borrower=request.user).filter(status='False')
    context={
        'books':lemda,
    }
    '''
    The above key books in dictionary context should contain a list of instances of the
    bookcopy model. Only those books should be included which have been loaned by the user.
    '''
    # START YOUR CODE HERE



    return render(request,template_name,context=context)

@csrf_exempt
@login_required
def loanBookView(request):

    '''
    Check if an instance of the asked book is available.
    If yes, then set message to 'success', otherwise 'failure'
    '''
    response_data={
         'message':None,
     }
    # START YOUR CODE HERE

    #if Book.objects.filter(id='request.POST.get("bid")').filter(status='1')
    book_id = request.POST.get("bid")
    response_data['message'] = 'failure'
    tv = Book.objects.get(id = book_id)
    try:
        temp = BookCopy.objects.get(book = Book.objects.get(id = book_id))
    except:
        response_data['message'] = 1
        BookCopy.objects.create(borrower = request.user,book = tv, borrow_date = datetime.datetime.now().date() )

    return JsonResponse(response_data)

'''
FILL IN THE BELOW VIEW BY YOURSELF.
This view will return the issued book.
You need to accept the book id as argument from a post request.
You additionally need to complete the returnBook function in the loaned_books.html file
to make this feature complete
'''
@csrf_exempt
@login_required
def returnBookView(request):
    response_data = {

         'message': None,
    }
    book_id = request.POST.get("bid")  # get the book id from post data
    #rating = request.POST['rating']
    lks = Book.objects.get(id = book_id)
    BookCopy.objects.filter(book = lks).update(
        status=True, borrow_date=None, borrower=None)
    BookCopy.objects.filter(book =lks).delete()
    response_data['message'] = 1
    return JsonResponse(response_data)
