"""sub_todo Views."""

# url(r'^$', views.render_index, name="index"),
# url(r'^add$', views.render_add_form, name="add_form"),
# url(r'^submit$', views.render_submit_ack, name="submit_ack"),
# url(r'^(?P<main_item_id>.+)/add$', views.render_subitem_add_form,
#     name="subitem_add_form"),
# url(r'^(?P<main_item_id>.+)/submit$', views.render_subitem_submit_ack,
#     name="subitem_submit_ack"),
# url(r'^(?P<main_item_id>.+)/(?P<sub_item_id>.+)/delete$', views.render_delete,
#     name="delete")


from django.shortcuts import render
from . import logic
from . import models

def render_index(request):
    """  """
    mainitems_to_subitems = logic.get_mainitems_to_subitems()
    template_list = {
        'mainitems': mainitems_to_subitems
    }
    return render(request, 'sub_todo/index.html', template_list)


def render_add_form(request):
    """Render the item add form."""
    return render(request, 'sub_todo/add_form.html')


def render_submit_ack(request):
    """Render the submission acknowledtement page."""
    model_name = request.POST['name']
    logic.create_save_new_main_item(model_name)
    item = models.MainItem.objects.get(name=model_name)
    item_id = item.id
    template_list = {
        'main_item_id': item_id
    }
    return render(request, 'sub_todo/submit_ack.html', template_list)


def render_subitem_add_form(request, main_item_id):
    """  """
    arguments = {
        'main_item_id': main_item_id
    }
    return render(request, 'sub_todo/subitem_add_form.html', arguments)


def render_subitem_submit_ack(request, main_item_id):
    """  """
    model_name = request.POST['name']
    main_item = models.MainItem.objects.get(id=main_item_id)
    logic.create_save_new_sub_item(model_name, main_item)
    sub_item = models.SubItem.objects.get(name=model_name)
    sub_item_id = sub_item.id
    template_list = {
        'sub_item_id': sub_item_id,
        'main_item_id': main_item_id
    }
    return render(request, 'sub_todo/subitem_submit_ack.html', template_list)



def render_delete(request, main_item_id, sub_item_id):
    """  """
    # logic.delete_subitem(sub_item_id, main_item_id)
    return render(request, 'sub_todo/delete.html')
