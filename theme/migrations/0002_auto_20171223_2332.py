# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-23 23:32
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='featured_gallery_heading',
            field=models.CharField(blank=True, default='Our clients', help_text='If present and featured_gallery is selected a carousel of the gallery images will be shown with this title.', max_length=100),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_portfolio_heading',
            field=models.CharField(blank=True, default='Recent works', help_text='If present and featured_portfolio is set portfolio items will be shown with this header.', max_length=100),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='icon_box_layout',
            field=models.CharField(choices=[('TW', 'Two across'), ('TH', 'Three across'), ('TB', 'Three across boxes')], default='TH', max_length=2),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='max_portfolio_items',
            field=models.PositiveIntegerField(blank=True, default=6, help_text='The maximum number of items from the above selected portoflio to show.', null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='recent_blog_heading',
            field=models.CharField(blank=True, default='Latest blog posts', help_text='If present recent blog posts will be shown', max_length=100),
        ),
        migrations.AlterField(
            model_name='iconbox',
            name='icon',
            field=models.CharField(help_text='Enter the name of a font awesome icon, i.e. fa-eye. A list is available here http://fontawesome.io/', max_length=50),
        ),
        migrations.AlterField(
            model_name='iconbox',
            name='link',
            field=models.CharField(blank=True, help_text='Optional, if provided clicking the box will go here.', max_length=2000),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='blog_layout',
            field=models.PositiveIntegerField(choices=[(1, 'One'), (2, 'Two')], default=2, help_text='Determines how many blog posts are shown per row in the blog list view'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='color_scheme',
            field=models.PositiveIntegerField(default=3, help_text='Use the cog icon in the front end to try out color schemes.'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='contact_iframe',
            field=models.TextField(blank=True, help_text="If present any form with slug contact will displayed with a custom template that has this iframe at the top. i.e. add a Google Map's iframe here."),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='contact_iframe_layout',
            field=models.CharField(blank=True, choices=[('FULL', 'Full width'), ('PAGE', 'Page width')], default='FULL', max_length=4),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='footer_blog_heading',
            field=models.CharField(default='Recent posts', max_length=100),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='footer_flickr_content',
            field=mezzanine.core.fields.RichTextField(blank=True, help_text='If present will override the flickr widget in the footer'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='footer_flickr_heading',
            field=models.CharField(default='Flickr photos', max_length=100),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='footer_menu_heading',
            field=models.CharField(default='Popular pages', max_length=100),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='sidebar_alignment',
            field=models.CharField(choices=[('LE', 'Left'), ('RI', 'Right')], default='RI', help_text='For pages that have a sidebar, determines if it is on the left or right', max_length=2),
        ),
        migrations.AlterField(
            model_name='slide',
            name='button_text',
            field=models.CharField(blank=True, help_text='Optional, if present a button with the link specified below will be in the slide', max_length=100),
        ),
        migrations.AlterField(
            model_name='slide',
            name='content',
            field=models.TextField(blank=True, help_text='Add <br> for line breaks'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='custom',
            field=models.TextField(blank=True, help_text='Create a custom slide, everything else will be overriden'),
        ),
    ]
