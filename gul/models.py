# gul/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User  # Импортируем кастомную модель пользователя

class Order(models.Model):
    # Статусы заказа (используем английские значения для консистентности)
    STATUS_CHOICES = [
        ('pending', _('Pending')),  # Перевод будет обрабатываться через i18n
        ('approved', _('Approved')),
        ('rejected', _('Rejected')),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name=_('User')
    )  # Связь с пользователем
    name = models.CharField(max_length=255, verbose_name=_('Name'))  # Имя пользователя
    product = models.CharField(max_length=255, verbose_name=_('Product'))  # Название продукта
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))  # Количество
    phone = models.CharField(max_length=20, verbose_name=_('Phone'))  # Телефон
    receipt = models.FileField(
        upload_to='receipts/',
        blank=True,
        null=True,
        verbose_name=_('Receipt')
    )  # Чек (необязательное поле)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name=_('Status')
    )  # Статус заказа
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))  # Дата создания
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))  # Дата обновления

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        ordering = ['-created_at']  # Сортировка по дате создания (новые сверху)

    def __str__(self):
        return f'Order #{self.id} - {self.product} by {self.name} ({self.status})'
