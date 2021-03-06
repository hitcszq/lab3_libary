from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from django.template import RequestContext
from lab3app.models import book,Author 
from django.template.response import TemplateResponse as TR
def index(request):
	return render_to_response('index.html')
def search(request):
	if 'author' in request.GET and request.GET['author']:
		get_author=request.GET['author']
		if  not Author.objects.filter(Name=get_author):
			return	render_to_response('add_author.html')
		else:
			authorID=Author.objects.filter(Name=get_author)[0]
			books=book.objects.filter(AuthorID=authorID.AuthorID)
			d = {'books':books}
		return TR(request,"search_result.html",d)
	else:
		return HttpResponse('submit a  right search term')
def search_info(request):
	if 'book_id' in request.GET and request.GET['book_id']:
		get_book=request.GET['book_id']
		book_need=book.objects.filter(id=get_book)[0]
		h={'book_need':book_need}
		return TR(request,"book_info.html",h)
	else:
		return HttpResponse('submit a search term')
def delete(request):
	if 'book_id' in request.GET and request.GET['book_id']:
		get_book=request.GET['book_id']
		book_needdelete=book.objects.filter(id=get_book)[0]
		book_needdelete.delete()
		return HttpResponse('you have succesfully delete the book')
	else:
		return HttpResponse('Nope,delete unsuccesful')
def add_book(request):
	if "book_name" in request.GET and "book_isbn" in request.GET and "book_author" in request.GET and "book_publisher" in request.GET and "book_publish_date" in request.GET:
		get_author=request.GET['book_author']
		b=Author.objects.filter(Name=get_author)
		if not b:
			return render_to_response('add_author.html')
		else:
			the_author=b[0]
			get_isbn=request.GET['book_isbn']
			get_publisher=request.GET['book_publisher']
			get_publishdate=request.GET['book_publish_date']
			get_title=request.GET['book_name']
			get_price=request.GET['book_price']
			new_book=book(ISBN=get_isbn,Title=get_title,AuthorID=the_author.AuthorID,Publisher=get_publisher,PublishDate=get_publishdate,Price=get_price)
			new_book.save()
			return HttpResponse('you have succesfully add the book')
	else:
		return HttpResponse('submit a right search term')
def add_author(request):
	if "author_name" in request.GET and "author_age" in request.GET and "author_country" in request.GET:
		get_name=request.GET['author_name']
		get_age=request.GET['author_age']
		get_country=request.GET['author_country']
		new_author=Author(Name=get_name,Age=get_age,Country=get_country)
		new_author.save()
		new_author_ob=Author.objects.filter(Name=get_name)[0]
		new_author_ob.AuthorID=new_author_ob.id
		new_author_ob.save()
		return HttpResponse('you have succesfully add the author')
	else:
		return HttpResponse('submit a search term')
def restore(request):
	if "book_id" in request.GET and request.GET['book_id']:
		the_id=request.GET['book_id']
		thebook=book.objects.filter(id=the_id)[0]
		thebook.delete()
		return render_to_response('restore.html')
def re_load(request):
	if "book_name" in request.GET and "book_isbn" in request.GET and "book_author" in request.GET and "book_publisher" in request.GET and "book_publish_date" in request.GET:
		get_author=request.GET['book_author']
		if  not Author.objects.filter(Name=get_author):
			return	render_to_response('add_author.html')
		else:
			the_author=Author.objects.filter(Name=get_author)[0]
			get_isbn=request.GET['book_isbn']
			get_publisher=request.GET['book_publisher']
			get_publishdate=request.GET['book_publish_date']
			get_title=request.GET['book_name']
			get_price=request.GET['book_price']
			new_book=book(ISBN=get_isbn,Title=get_title,AuthorID=the_author.AuthorID,Publisher=get_publisher,PublishDate=get_publishdate,Price=get_price)
			new_book.save()
			return HttpResponse('you have succesfully reload the book')
	else:
		return HttpResponse('submit a right search term')
# Create your views here.
