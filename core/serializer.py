from rest_framework import serializers
from core.models import Order, Stocks
from django.db.models import Sum


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'order_type', 'stock', 'quantity')
        read_only_fields = ('user',)


class TotalValueSerializer(serializers.ModelSerializer):
    stock_price = serializers.SerializerMethodField()
    total_value = serializers.SerializerMethodField()
    stock_id = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ('user_id', 'stock_id','stock_price', 'order_type', 'total_value' )
        read_only_fields = ('user_id', 'stock_price')
    
    def get_stock_price(self, obj):
        stock_id = self.context['request'].data['stock_id']
        global stock_price
        stock_price = list(Stocks.objects.filter(id = stock_id).values('price'))[0]['price']
        return stock_price

    def get_user_id(self, obj):
        global user_id
        user_id = self.context['request'].data['user_id']
        return user_id
    
    def get_stock_id(self, obj,):
        global stock_id
        stock_id = self.context['request'].data['stock_id']
        return stock_id
    
    def get_total_value(self, obj):
        print(stock_price)
        order_type = self.context['request'].data['order_type']
        total_order = Order.objects.filter(user_id = user_id,stock_id = stock_id,order_type = order_type).aggregate(Sum('quantity'))
        # return int(total_order['quantity__sum']) * float(stock_price)
        return int(total_order['quantity__sum']) * float(stock_price)


        

