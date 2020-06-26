from django.shortcuts import get_object_or_404


def delete(model, id):
    new_model = get_object_or_404(model, id=id)
    new_model.state = 0
    new_model.save()
    return True
