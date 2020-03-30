from rest_framework import serializers

client_link = serializers.HyperlinkedIdentityField(
    view_name='confma:client_detail',
    lookup_field='id'
)

cloth_link = serializers.HyperlinkedIdentityField(
    view_name='confma:cloth_detail',
    lookup_field='id'
)

quotation_link = serializers.HyperlinkedIdentityField(
    view_name='confma:quotation_detail',
    lookup_field='id'
)

rental_link = serializers.HyperlinkedIdentityField(
    view_name='confma:rental_detail',
    lookup_field='id'
)

quotation_client_link = serializers.HyperlinkedIdentityField(
    view_name='confma:quotation_client_detail',
    lookup_field='id'
)
