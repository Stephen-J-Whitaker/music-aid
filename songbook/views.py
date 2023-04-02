from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View, generic
from .models import Song, Setlist
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django import forms
from .forms import SongAddForm, SetlistAddForm
from django_summernote.widgets import SummernoteWidget
from django.urls import reverse_lazy, reverse


class SongbookList(generic.ListView):
    """
    Class based view to show the users
    songbook list
    """
    model = Song
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """
        Add a page title context
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Music Aid Songbook'
        return context

    def get_queryset(self):
        """
        Define the queryset to be used
        """
        if self.request.user.id is not None:
            user = self.request.user
            return Song.objects.filter(user=user).order_by('title')


class SongAdd(LoginRequiredMixin, generic.CreateView):
    form_class = SongAddForm
    # Code supplied by Code Institute Tutor Support
    model = Song
    template_name = 'song_add_edit.html'
    # End of code supplied by Code Institute Tutor Support
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        """
        Add contexts
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a song to songbook'
        context['mode'] = 'add'
        return context

    def form_valid(self, form):
        """
        Add the user primary key to the form
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class SongView(LoginRequiredMixin, generic.DetailView):
    """
    A class based view to view a song
    """
    context_object_name = 'song_detail'
    template_name = 'song_view.html'

    def get_context_data(self, **kwargs):
        """
        Add contexts
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'View a song'
        context['pk'] = self.kwargs['pk']
        return context

    def get_queryset(self):
        """
        Define the queryset to be used
        """
        return Song.objects.filter(user=self.request.
                                   user).filter(pk=self.kwargs['pk'])


class SongEdit(LoginRequiredMixin, generic.UpdateView):
    """
    A class based view to edit a song
    """
    form_class = SongAddForm
    template_name = 'song_add_edit.html'

    def get_context_data(self, **kwargs):
        """
        Add contexts
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit a song'
        context['mode'] = 'edit'
        context['pk'] = self.kwargs['pk']
        return context

    def get_queryset(self):
        """
        Define the queryset to be used
        """
        return Song.objects.filter(user=self.request.
                                   user).filter(pk=self.kwargs['pk'])

    def get_success_url(self, **kwargs):
        """
        If success send back to correct song view
        """
        return reverse('song_view', kwargs={'pk': self.object.pk})


class SongDelete(LoginRequiredMixin, generic.DeleteView):
    """
    A class based view to confirm a deletion of a song
    """
    model = Song
    success_url = reverse_lazy('home')
    template_name = 'song_confirm_delete.html'

    def get_queryset(self):
        """
        Define the queryset to be used
        """
        return Song.objects.filter(user=self.request.
                                   user).filter(pk=self.kwargs['pk'])


class SetlistAdd(LoginRequiredMixin, View):
    """
    A class based view to add setlists
    """

    def get(self, request, *args, **kwargs):
        """
        Get handling to render SetlistAddForm
        """
        setlist_add_form = SetlistAddForm(data=request.POST, user=request.user)

        return render(
            request,
            "setlist_add_edit.html",
            {
                "setlist_add_form": SetlistAddForm(data=request.POST,
                                                   user=request.user)
            },
        )

    def post(self, request, *args, **kwargs):
        """
        Post handling for SetlistAddForm
        """
        setlist_add_form = SetlistAdd(data=request.POST, user=request.user)

        if setlist_add_form.is_valid():
            setlist_add_form.save()

        return render(
            request,
            "setlist_add_edit.html",
            {
                "setlist_add_form": SetlistAddForm(data=request.POST,
                                                   user=request.user)
            },
        )


class SetlistList(generic.ListView):
    """
    Class based view to show the users
    list of setlists
    """
    model = Setlist
    template_name = 'setlist_list.html'

    def get_context_data(self, **kwargs):
        """
        Add a page title context
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'View your setlists'
        return context

    def get_queryset(self):
        """
        Define the queryset to be used
        """
        if self.request.user.id is not None:
            user = self.request.user
            return Setlist.objects.filter(user=user).order_by('setlist_name')
