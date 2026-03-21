from django.db import models

class ProductSet(models.Model):
    title = models.CharField(max_length=200, verbose_name="Топтомдун аталышы")
    pieces = models.IntegerField(verbose_name="Даана саны")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Баасы (сом)")
    
    # ЖАҢЫ: Даяр болуу убактысы
    ready_time = models.CharField(
        max_length=100, 
        verbose_name="Даяр болуу убактысы", 
        help_text="Мисалы: 2-3 саат же 1 күн",
        default="2 саат"
    )
    
    image = models.ImageField(upload_to='sets/', verbose_name="Сүрөтү")
    whatsapp_msg = models.TextField(
        verbose_name="WhatsApp билдирүүсү", 
        help_text="Кардар 'Заказ берүү' баскычын басканда сизге келе турган текст"
    )

    def __str__(self):
        return f"{self.title} ({self.pieces} даана)"

    class Meta:
        verbose_name = "Топтом"
        verbose_name_plural = "Топтомдор"