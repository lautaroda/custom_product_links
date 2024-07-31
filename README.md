# Product Move Links

## Descripción

El módulo `Product Move Links` agrega enlaces a los documentos relacionados (órdenes de compra y órdenes de venta) en la vista de lista de las líneas de movimientos de stock en Odoo. Esto permite acceder directamente a los documentos relacionados desde la vista de lista, mejorando la eficiencia y la facilidad de uso.

## Características

- Añade un campo `related_document_link` a las líneas de movimientos de stock.
- Calcula y muestra enlaces URL a los documentos relacionados (órdenes de compra y órdenes de venta).
- Los enlaces son clicables y abren los documentos relacionados en una nueva pestaña.

## Instalación

1. Clona este repositorio en tu directorio de addons de Odoo.

   ```sh
   git clone ...
Reinicia el servidor de Odoo para cargar el nuevo módulo.


sudo service odoo restart
Ve a Apps en la interfaz de usuario de Odoo.

Haz clic en Actualizar lista de aplicaciones.

Busca Product Move Links y haz clic en Instalar.

Uso
Navega a Inventario > Operaciones > Transferencias.
Abre una transferencia de stock.
En la vista de lista de las líneas de movimientos de stock, verás un nuevo campo related_document_link.
Haz clic en el enlace para abrir el documento relacionado en una nueva pestaña.
Configuración
Este módulo no requiere configuración adicional. El enlace se genera automáticamente basado en el campo origin de la línea de movimiento de stock.

Dependencias
stock
Autor
Lautaro  De Angelis
Licencia
Este módulo está licenciado bajo los términos de la Licencia MIT.

Contacto
Para soporte y consultas, por favor contacta a lautarodeangelis@gmail.com.



### Instrucciones

1. **Clona el repositorio**: Usa el comando `git clone` para clonar el repositorio en tu directorio de addons de Odoo.
2. **Reinicia Odoo**: Reinicia tu servidor de Odoo para cargar el nuevo módulo.
3. **Instala el módulo**: Ve a `Apps` en la interfaz de usuario de Odoo, actualiza la lista de aplicaciones e instala `Product Move Links`.





