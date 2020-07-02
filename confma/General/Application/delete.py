from django.shortcuts import get_object_or_404


def delete(model, id):
    get_model = get_object_or_404(model, id=id)
    get_model.state = 0
    get_model.save()
    return True
