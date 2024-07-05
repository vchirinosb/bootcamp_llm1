"""
Tarea 05.
Github: https://github.com/vchirinosb/bootcamp_llm1/blob/main/tarea05.py
Pull Request: https://github.com/vchirinosb/bootcamp_llm1/pull/5
"""
from datetime import date


class Categoria:

    """Clase Categoria."""

    def __init__(self, nombre: str, descripcion: str):
        self._nombre = nombre
        self._descripcion = descripcion
    
    def __str__(self) -> str:
        return f'{self._nombre}'
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str):
        self._nombre = valor

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor: str):
        self._descripcion = valor


class Proveedor:

    """Clase Proveedor."""

    def __init__(self, nombre: str, direccion: str, telefono: str, email: str):
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._email = email
    
    def __str__(self) -> str:
        return f'{self._nombre}'
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str):
        self._nombre = valor
    
    @property
    def direccion(self) -> str:
        return self._direccion
    
    @direccion.setter
    def direccion(self, valor: str):
        self._direccion = valor
    
    @property
    def telefono(self) -> str:
        return self._telefono
    
    @telefono.setter
    def telefono(self, valor: str):
        self._telefono = valor
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, valor: str):
        self._email = valor


class Producto:

    """Clase Producto."""

    def __init__(
            self, nombre: str, descripcion: str, precio: float,
            categoria: Categoria, proveedor: Proveedor, cantidad_stock: int):
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._categoria = categoria
        self._proveedor = proveedor
        self._cantidad_stock = cantidad_stock
    
    def __str__(self) -> str:
        return f'{self._nombre}'
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str):
        self._nombre = valor

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor: str):
        self._descripcion = valor
    
    @property
    def precio(self) -> float:
        return self._precio
    
    @precio.setter
    def precio(self, valor: float):
        self._precio = valor

    @property
    def categoria(self) -> Categoria:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: Categoria):
        self._categoria = valor
    
    @property
    def proveedor(self) -> Proveedor:
        return self._proveedor

    @proveedor.setter
    def proveedor(self, valor: Proveedor):
        self._proveedor = valor

    @property
    def cantidad_stock(self) -> int:
        return self._cantidad_stock
    
    @cantidad_stock.setter
    def cantidad_stock(self, valor: int):
        self._cantidad_stock = valor
    
    def actualizar_stock(self, cantidad: int):
        """Actualiza el stock de un producto."""
        if self._cantidad_stock + cantidad < 0:
            raise ValueError('No se puede tener un stock negativo.')
        self._cantidad_stock += cantidad
    
    def actualizar_precio(self, nuevo_precio: float):
        """Actualiza el precio del producto."""
        if nuevo_precio < 0:
            raise ValueError('El precio no puede ser negativo.')
        self._precio = nuevo_precio
    
    def verificar_stock(self, cantidad: int) -> bool:
        """Verifica si hay suficiente stock para una cantidad dada."""
        return self._cantidad_stock >= cantidad
    
    def mostrar_informacion(self) -> str:
        """Retorna la información del producto."""
        return (
            f'Producto: {self._nombre}\n'
            f'Descripción: {self._descripcion}\n'
            f'Precio: {self._precio:.2f} soles\n'
            f'Stock: {self._cantidad_stock} unidades\n'
            f'Categoría: {self._categoria._nombre}\n'
            f'Proveedor: {self._proveedor._nombre}\n')


class ProductoDigital(Producto):

    """Clase Producto Digital."""

    def __init__(
            self, nombre: str, descripcion: str, precio: float,
            categoria: Categoria, proveedor: Proveedor, url_descarga: str,
            tamanio_archivo: str):
        super().__init__(
            nombre, descripcion, precio, categoria, proveedor,
            cantidad_stock=0)
        self._url_descarga = url_descarga
        self._tamanio_archivo = tamanio_archivo

    @property
    def url_descarga(self) -> str:
        return self._url_descarga
    
    @url_descarga.setter
    def url_descarga(self, valor: str):
        self._url_descarga = valor
    
    @property
    def tamanio_archivo(self) -> str:
        return self._to_tamanio_archivotal
    
    @tamanio_archivo.setter
    def tamanio_archivo(self, valor: str):
        self._tamanio_archivo = valor
    
    def actualizar_stock(self, cantidad: int):
        """Este método no aplica para productos digitales."""
        raise NotImplementedError('Stock no aplica para el Producto Digital')
    
    def verificar_stock(self, cantidad: int) -> bool:
        """Retorna True, stock no aplica para Producto Digital."""
        return True
    
    def mostrar_informacion(self) -> str:
        """Retorna la información del producto."""
        return (
            f'Producto: {self._nombre}\n'
            f'Descripción: {self._descripcion}\n'
            f'Precio: {self._precio:.2f} soles\n'
            f'Categoría: {self._categoria._nombre}\n'
            f'Proveedor: {self._proveedor._nombre}\n'
            f'URL de descarga: {self._url_descarga}\n'
            f'Tamaño del archivo: {self._tamanio_archivo}')


class Venta:

    """Clase Venta."""

    def __init__(self, fecha: date):
        self._productos = []
        self._fecha = fecha
        self._total = 0.0
    
    def __str__(self) -> str:
        return f'{self._fecha} - {self._total}'

    @property
    def fecha(self) -> date:
        return self._fecha
    
    @fecha.setter
    def fecha(self, valor: date):
        self._fecha = valor
    
    @property
    def total(self) -> float:
        return self._total
    
    @total.setter
    def total(self, valor: float):
        self._total = valor
    
    def agregar_producto(self, producto: Producto, cantidad: int):
        """
        Agregar un producto a la venta, verificar stock y calcular el total.
        """
        if not producto.verificar_stock(cantidad):
            raise ValueError(
                f'Stock carente para el producto: {producto._nombre}.')

        # Añadir producto y cantidad a la lista de productos.
        self._productos.append((producto, cantidad))

        # Actualizar stock del producto (sólo para producto físico).
        if not isinstance(producto, ProductoDigital):
            producto.actualizar_stock(-cantidad)
        
        # Calcular nuevo total.
        self._total += producto._precio * cantidad

    def eliminar_producto(self, producto: Producto):
        """
        Eliminar un producto de la venta, ajustar el stock y recalcular el total.
        """
        for indice, (item, cantidad) in enumerate(self._productos):
            if item == producto:
                # Actualizar stock del producto (sólo para producto físico).
                if not isinstance(producto, ProductoDigital):
                    producto.actualizar_stock(cantidad)

                # Calcular nuevo total.
                self._total -= producto._precio * cantidad
                
                # Eliminar el producto de la venta.
                del self._productos[indice]
                return
        raise ValueError(
            f'El producto: {producto._nombre} no esta listado en la venta.')
    
    def mostrar_informacion(self) -> str:
        """Devuelve una cadena con la información de la venta."""
        listado_productos = '\n'.join(
            f"Producto: {producto._nombre} - Cantidad: {cantidad} - Subtotal: {producto._precio * cantidad:.2f} soles"
            for producto, cantidad in self._productos
        )

        return (    
            f"Fecha: {self._fecha.strftime('%m/%d/%Y')}\n"
            f"Listado de productos: \n{listado_productos}\n"
            f"Total: {self._total:.2f} soles")


if __name__ == '__main__':
    """Ejemplo de Ejecución."""
    # Agregar Proveedores.
    proveedor_1 = Proveedor(
        'Nicolini SA', 'Av. Javier Prado 123', '+51 987654321',
        'ventas@nicolini.com')
    proveedor_2 = Proveedor(
        'Peru EBooks', '123 Madison Avenue', '+1 98761234',
        'soporte@peruebooks.com')
    
    # Agregar Categorías.
    categoria_1 = Categoria('Pastas', 'Fideos de harina de trigo')
    categoria_2 = Categoria(
        'E-books Fotografia', 'E-books orientados a la fotografia profesional')

    # Agregar Productos físicos.
    producto_1 = Producto(
        'Fusilli', 'Fusilli de harina de trigo', 3.5, categoria_1, proveedor_1,
        150)
    producto_2 = Producto(
        'Farfale', 'Farfale de harina de trigo', 3.7, categoria_1, proveedor_1,
        200)
    producto_3 = Producto(
        'Fettuccine', 'Fettuccine de harina de trigo', 3.1, categoria_1,
        proveedor_1, 180)

    # Agregar Productos digitales.
    producto_4 = ProductoDigital(
        'Mejora tus fotos', 'Aprende fotografía básica y mejora tus fotos',
        39.9, categoria_2, proveedor_2, 'http://example.com/download/1',
        '12MB')
    producto_5 = ProductoDigital(
        'Guia para un shooting',
        'Todos los concejos para preparar un shooting perfecto', 48.0,
        categoria_2, proveedor_2, 'http://example.com/download/2', '20MB')
    producto_6 = ProductoDigital(
        'Guía de Fotografía para Bloggers',
        'Todo lo que debes de conocer para mejorar tus fotografías y triunfar '
        'en tu blog', 53.0, categoria_2, proveedor_2,
        'http://example.com/download/3', '18MB')
    
    # Mostrar información de un producto físico y un producto digital.
    print("Producto físico:")
    print(producto_1.mostrar_informacion())
    print('-----------------')
    print("Producto digital:")
    print(producto_4.mostrar_informacion())
    print('-----------------')

    # Crear una venta
    venta_1 = Venta(date.today())

    # Agregar productos al registro de Venta.
    venta_1.agregar_producto(producto_2, 5)
    venta_1.agregar_producto(producto_3, 4)
    venta_1.agregar_producto(producto_5, 1)
    venta_1.agregar_producto(producto_6, 1)

    # Mostrar información de la venta.
    print("Información registro de venta:")
    print(venta_1.mostrar_informacion())
    print('-----------------')

    # Eliminar productos de la venta.
    venta_1.eliminar_producto(producto_3)
    venta_1.eliminar_producto(producto_6)

    # Mostrar información de la venta.
    print("Información registro de venta:")
    print(venta_1.mostrar_informacion())
    print('-----------------')

    # Verificar stock de los productos después de la venta realizada.
    print('Información de Productos:')
    print(producto_2.mostrar_informacion())
    print('-----------------')
    print(producto_3.mostrar_informacion())
