from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View, generic
from .models import Song, Setlist
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify
from django import forms
from .forms import SongAddForm, SetlistAddForm, SetlistEditForm
from django_summernote.widgets import SummernoteWidget
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


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


class SongAdd(SuccessMessageMixin, LoginRequiredMixin,
              generic.CreateView):
    form_class = SongAddForm
    # Code supplied by Code Institute Tutor Support
    model = Song
    template_name = 'song_add_edit.html'
    # End of code supplied by Code Institute Tutor Support
    success_message = "Your song has been added"
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
    model = Song
    context_object_name = 'song_detail'
    template_name = 'song_view.html'

    def get_context_data(self, **kwargs):
        """
        Add contexts
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'View a song'
        context['pk'] = self.kwargs['pk']
        context['setlist_pk'] = self.kwargs.get('setlist_pk', None)
        return context


class SongEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    """
    A class based view to edit a song
    """
    form_class = SongAddForm
    template_name = 'song_add_edit.html'
    success_message = "Your song has been edited"

    def get_context_data(self, **kwargs):
        """
        Add contexts
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit a song'
        context['mode'] = 'edit'
        context['pk'] = self.kwargs['pk']
        context['setlist_pk'] = self.kwargs.get('setlist_pk', None)
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
        setlist_pk = self.kwargs.get('setlist_pk', None)
        if setlist_pk is None:
            return reverse('song_view', kwargs={'pk': self.object.pk})
        else:
            return reverse('setlist_song_view', kwargs={
                'pk': self.object.pk,
                'setlist_pk': setlist_pk},
                )


class SongDelete(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    """
    A class based view to confirm a deletion of a song
    """
    model = Song
    template_name = 'song_confirm_delete.html'
    success_message = "Your song has been deleted"

    def get_context_data(self, **kwargs):
        """
        Add contexts
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Confirm a song deletion'
        context['pk'] = self.kwargs['pk']
        context['setlist_pk'] = self.kwargs.get('setlist_pk', None)
        return context

    # Code sourced from stackoverflow.com:
    # questions/24822509/success-message-in-deleteview-not-shown
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(SongDelete, self).delete(request, *args, **kwargs)
    # End of code sourced from stackoverflow
    # questions/24822509/success-message-in-deleteview-not-shown

    def get_success_url(self, **kwargs):
        """
        If success send back to correct view
        """
        setlist_pk = self.kwargs.get('setlist_pk', None)
        if setlist_pk is None:
            return reverse_lazy('home')
        else:
            return reverse('setlist_view', kwargs={'pk': setlist_pk})


class SetlistAdd(SuccessMessageMixin, LoginRequiredMixin,
                 generic.CreateView):
    """
    A class based view to add setlists
    """
    model = Setlist
    form_class = SetlistAddForm
    template_name = 'setlist_add_edit.html'
    success_message = "Your setlist has been added"

    def get_context_data(self, **kwargs):
        """
        Add contexts
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a setlist to songbook'
        context['mode'] = 'add'
        return context

    def get_initial(self):
        """
        Pass the user to SetlistAddForm
        """
        self.initial.update({'user': self.request.user})
        return self.initial

    def form_valid(self, form):
        """
        Add the user primary key to the form
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        """
        If success send back to correct setlist list
        """
        return reverse('setlist_list')


class SetlistList(LoginRequiredMixin, generic.ListView):
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


class SetlistView(LoginRequiredMixin, generic.ListView):
    """
    A class based view for view a set of songs
    """
    model = Setlist
    context_object_name = 'setlist_detail'
    template_name = 'setlist_view.html'

    def get_context_data(self, **kwargs):
        """
        Add contexts
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'View the songs in your setlist'
        setlist_object = Setlist.objects.get(pk=self.kwargs['pk'])
        context['setlist_name'] = setlist_object.setlist_name
        context['pk'] = self.kwargs['pk']
        return context

    def get_queryset(self):
        """
        Define the queryset to be used
        """
        set = Setlist.objects.get(pk=self.
                                  kwargs['pk']).songs_in_setlist.all()

        return Setlist.objects.get(pk=self.
                                   kwargs['pk']).songs_in_setlist.all()


class SetlistEdit(LoginRequiredMixin, View):
    """
    A class based view to edit setlists
    """

    def get(self, request, *args, **kwargs):
        """
        Get handling to render SetlistAddForm
        """
        form = SetlistEditForm(user=request.user, setlist_pk=self.kwargs['pk'])

        return render(
            request,
            "setlist_add_edit.html",
            {
                "title": "Create a setlist",
                "setlist_pk": self.kwargs['pk'],
                "mode": "edit",
                "form": SetlistEditForm(user=request.user,
                                        setlist_pk=self.kwargs['pk']),
            },
        )

    def post(self, request, *args, **kwargs):
        """
        Post handling for SetlistAddForm
        """
        form = SetlistEditForm(data=request.POST, user=request.user,
                               setlist_pk=self.kwargs['pk'])

        if form.is_valid():
            setlist = form.save(commit=False)
            setlist.user = request.user
            setlist.pk = self.kwargs['pk']
            setlist.save()
            form.save_m2m()
            messages.add_message(request, messages.SUCCESS, 'Your setlist has'
                                                            ' been edited')

        return redirect('setlist_view', self.kwargs['pk'])


class SetlistDelete(SuccessMessageMixin, LoginRequiredMixin,
                    generic.DeleteView):
    """
    A class based view to confirm a deletion of a song
    """
    model = Setlist
    success_url = reverse_lazy('setlist_list')
    template_name = 'setlist_confirm_delete.html'
    success_message = "Your setlist has been deleted"

    def get_context_data(self, **kwargs):
        """
        Add contexts
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Confirm a setlist deletion'
        context['pk'] = self.kwargs['pk']
        return context

    # Code sourced from stackoverflow.com:
    # questions/24822509/success-message-in-deleteview-not-shown
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(SetlistDelete, self).delete(request, *args, **kwargs)
    # End of code sourced from stackoverflow


def handler404(request, exception):
    """
    Load 404 page if item not found
    """
    return render(request, '404.html')
