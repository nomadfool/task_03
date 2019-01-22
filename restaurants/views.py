from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list" : [
    	{
    		"restaurant_name" : "Happy Clam",  
    		"food_type" : "Sea food"
    	},
    	{
    		"restaurant_name" : "Jolly Rancher", 
    		"food_type" : "Lots of meat"
    	},
    	{
    		"restaurant_name" : "Fancy Italian Name", 
    		"food_type" : "Italian"
    	}
    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object" : {
    		"restaurant_name" : "Happy Clam",  
    		"food_type" : "Sea food"
    	}

    }
    return render(request, 'detail.html', context)
