'''
    <strong>Name:</strong> {{ product.name }}<br>
                    <strong>Description:</strong> {{ product.description }}<br>
                    <strong>Category:</strong> {{ product.category }}<br>
                    <strong>Variants:</strong>

                        {% for variant in product.productvariants_set.all %}
                            <strong>Brand:</strong> {{ variant.variant.brand }}<br>
                                <img class="thumbnail" src="{{ variant.variant.image.url }}" >

                            <li>
                                {{ variant.product_variant_name }} - SKU: {{ variant.sku }} - Price: ${{ variant.price }}
                                <ul>
                                    {% for value in variant.variantvalue_set.all %}
                                        <li>ahhssssssssssssss{{ value.variant.variant }}: {{ value.value }}</li>
                                    {% endfor %}
                                </ul>
                            </li>
                    {% endfor %}
'''