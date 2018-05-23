"""Import everything we expose in crudlfap namespace."""

from django.utils.module_loading import import_string

from .apps import _installed
from .factory import Factory
from .registry import Registry
from .route import Route
from .router import Router, Views, ViewsDescriptor
from .site import site
from .views.debug import UrlsView
from .views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    HistoryView,
    ModelViewMixin,
    ObjectFormView,
    ObjectView,
    ObjectViewMixin,
    TemplateView,
    UpdateView,
    View,
    ViewMixin,
)
from .views.list import (
    BaseListView,
    FilterMixin,
    ListView,
    SearchMixin,
    TableMixin,
)
from .views.lock import LockViewMixin
