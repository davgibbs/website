# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import core.models
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0002_auto_20160518_1158'),
        ('core', '0008_auto_20150821_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvancedPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, auto_created=True, to='wagtailcore.Page')),
                ('show_meetups', models.BooleanField(default=False)),
                ('show_sponsors', models.BooleanField(default=False)),
                ('body', wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='title')), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.RichTextBlock()), ('alignment', core.models.ImageFormatChoiceBlock())), label='Aligned image', icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('aligned_html', wagtail.wagtailcore.blocks.StructBlock((('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('alignment', core.models.HTMLAlignmentChoiceBlock())), label='Raw HTML', icon='code')), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))))),
            ],
            options={
                'verbose_name': 'Advanced Page',
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
