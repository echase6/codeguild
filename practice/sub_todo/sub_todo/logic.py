"""sub_todo Logic."""

from . import models


def create_save_new_main_item(name):
    """  """
    new_item = models.MainItem(name=name)
    new_item.save()


def create_save_new_sub_item(name, main):
    """  """
    new_item = models.SubItem(name=name, main_parent=main)
    new_item.save()

def get_mainitems_to_subitems():
    mainitems = models.MainItem.objects.all()
    mainitems_to_subitems = []
    for item in mainitems:
        subitems = []
        for subitem in models.SubItem.objects.filter(main_parent=item):
            subitems.append({'name': subitem.name,
                             'id': subitem.id})
        mainitems_to_subitems.append({'name': item.name,
                                      'id': item.id,
                                      'subitems': subitems})
    return mainitems_to_subitems

def delete_subitem(sub_item_id, main_item_id):
    subitem = models.SubItem.objects.get(id=sub_item_id)
    subitem.delete()
    main_item = models.MainItem.objects.get(id=main_item_id)
    if len(models.SubItem.objects.filter(main_parent=main_item)) == 0:
        main_item.delete()


# return {item.name: [subitem.name
    #         for item in mainitems}


