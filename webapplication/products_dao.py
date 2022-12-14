from sql_connect import get_sql_connect


def get_all_products(connection, email):
    cursor = connection.cursor()

    query = "SELECT * FROM products where emailID=%s "
    cursor.execute(query, (email,))

    response = []

    for (id, name, code, size, quantity, pbf, paf, finalprice, emailID) in cursor:
        response.append(
            {
                'id': id,
                'name': name,
                'code': code,
                'size': size,
                'quantity': quantity,
                'pbf': pbf,
                'paf': paf,
                'finalprice': finalprice,
                'emailID': emailID
            }
        )

    return response




def insert_new_product(connection, products):
    cursor = connection.cursor()
    query = 'INSERT INTO products ' \
            '(name, code, size, quantity, pbf, paf, finalprice, emailID)' \
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'

    data = (products['name'], products['code'], products['size'], products['quantity'], products['pbf'],
            products['paf'], products['finalprice'], products['emailID'])

    cursor.execute(query, data)
    connection.commit()

    return "success"


def edit_product(connection, products):
    cursor = connection.cursor()

    query = 'UPDATE products SET name=%s, code=%s, size=%s, quantity=%s, pbf=%s, paf=%s, finalprice=%s WHERE ' \
            'id=%s '

    data = (products['name'], products['code'], products['size'], products['quantity'], products['pbf'],
            products['paf'], products['finalprice'], products['id'])

    cursor.execute(query, data)
    connection.commit()

    return "success"



def delete_product(connection, id):
    cursor = connection.cursor()
    id = "'" + id + "'"
    query = "DELETE FROM dbweb.products where id=" + id
    cursor.execute(query)
    connection.commit()


if __name__ == '__main__':
    connection = get_sql_connect()
    print(delete_product(connection, '"%s"'))
