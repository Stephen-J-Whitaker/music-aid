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
        return context


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

    def get_context_data(self, **kwargs):
        """
        Add contexts
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Confirm a song deletion'
        context['pk'] = self.kwargs['pk']
        return context


# class SetlistAdd(LoginRequiredMixin, View):
#     """
#     A class based view to add setlists
#     """

#     def get(self, request, *args, **kwargs):
#         """
#         Get handling to render SetlistAddForm
#         """
#         setlist_add_form = SetlistAddForm(data=request.POST, user=request.user)

#         return render(
#             request,
#             "setlist_add_edit.html",
#             {
#                 "title": "Create a setlist",
#                 "setlist_add_form": SetlistAddForm(data=request.POST,
#                                                    user=request.user),
#             },
#         )

#     def post(self, request, *args, **kwargs):
#         """
#         Post handling for SetlistAddForm
#         """
#         setlist_add_form = SetlistAdd(data=request.POST, user=request.user)

#         if setlist_add_form.is_valid():
#             setlist = setlist_add_form.save(commit=False)
#             setlist.user = request.user
#             setlist_add_form.save_m2m()

#         return render(
#             request,
#             "setlist_add_edit.html",
#             {
#                 "title": "Create a setlist",
#                 "setlist_add_form": SetlistAddForm(data=request.POST,
#                                                    user=request.user),
#             },
#         )

class SetlistAdd(LoginRequiredMixin, generic.CreateView):
    """
    A class based view to add setlists
    """
    model = Setlist
    form_class = SetlistAddForm
    template_name = 'setlist_add_edit.html'

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


# class SetlistEdit(LoginRequiredMixin, generic.UpdateView):
#     """
#     A class based view to edit a setlist
#     """
#     form_class = SetlistAddForm
#     template_name = 'setlist_add_edit.html'

#     def get_context_data(self, **kwargs):
#         """
#         Add contexts
#         """
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Edit a setlist'
#         context['mode'] = 'edit'
#         context['pk'] = self.kwargs['pk']
#         return context

#     def get_initial(self):
#         """
#         Pass the user to SetlistAddForm
#         """
#         self.initial.update({'user': self.request.user})
#         self.initial.update({'setlist_pk': self.kwargs['pk']})
#         return self.initial

#     def get_queryset(self):
#         """
#         Define the queryset to be used
#         """
#         return Setlist.objects.filter(user=self.request.
#                                       user).filter(pk=self.kwargs['pk'])

#     def get_success_url(self, **kwargs):
#         """
#         If success send back to correct song view
#         """
#         return reverse('setlist_view', kwargs={'pk': self.object.pk})

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
            print("set name field in form ", form.instance.setlist_name)
            print("form instance ", form.instance)
            setlist = form.save(commit=False)
            print("set name from commited ", setlist.setlist_name)
            setlist.user = request.user
            setlist.pk = self.kwargs['pk']
            setlist.save()
            form.save_m2m()

        # return HttpResponseRedirect(reverse('setlist_view', pk=[self.kwargs['pk']]))
        return redirect('setlist_view', self.kwargs['pk'])


class SetlistSongView(LoginRequiredMixin, generic.DetailView):
    """
    A class based view to view a song from a setlist
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
        context['setlist_pk'] = self.kwargs['setlist_pk']
        return context
