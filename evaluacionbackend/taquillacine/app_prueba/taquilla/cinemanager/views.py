from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView, View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Pelicula, Horario, Asiento
from .forms import HorarioForm, AsientoForm
from django.shortcuts import render, redirect
from django.urls import reverse


class ListaPeliculasView(ListView):
    model = Pelicula
    template_name = './peliculas/pelicula_list.html'
    context_object_name = 'peliculas'

class DetallePeliculaView(DetailView):
    model = Pelicula
    template_name = 'peliculas/detalle_pelicula.html'
    context_object_name = 'pelicula'

class CrearPeliculaView(CreateView):
    model = Pelicula
    template_name = 'peliculas/crear_pelicula.html'
    fields = ['titulo', 'clasificacion', 'genero', 'director']
    success_url = reverse_lazy('cineapp:lista_peliculas')

class ActualizarPeliculaView(UpdateView):
    model = Pelicula
    template_name = 'peliculas/actualizar_pelicula.html'
    fields = ['titulo', 'clasificacion', 'genero', 'director']
    success_url = reverse_lazy('cineapp:lista_peliculas')

class EliminarPeliculaView(DeleteView):
    model = Pelicula
    template_name = 'peliculas/eliminar_pelicula.html'
    success_url = reverse_lazy('cineapp:lista_peliculas')


class ListaHorariosPeliculaView(ListView):
    model = Horario
    template_name = 'horarios/lista_horarios_pelicula.html'
    context_object_name = 'horarios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pelicula_id = self.kwargs['pelicula_id']
        context['pelicula'] = Pelicula.objects.get(pk=pelicula_id) 
        return context

    def get_queryset(self):
        pelicula_id = self.kwargs['pelicula_id']
        return Horario.objects.filter(pelicula__id=pelicula_id)

def agregar_horario(request, pelicula_id):
    pelicula = Pelicula.objects.get(id=pelicula_id)

    if request.method == 'POST':
        form = HorarioForm(request.POST)
        if form.is_valid():
            horario = form.save(commit=False)
            horario.pelicula = pelicula
            horario.save()
            return redirect('cineapp:lista_horarios_pelicula', pelicula_id=pelicula_id)
    else:
        form = HorarioForm()

    return render(request, 'horarios/crear_horario.html', {'form': form, 'pelicula': pelicula})

def editar_horario(request, horario_id):
    horario = get_object_or_404(Horario, id=horario_id)

    if request.method == 'POST':
        form = HorarioForm(request.POST, instance=horario)
        if form.is_valid():
            form.save()
            return redirect('cineapp:lista_horarios_pelicula', pelicula_id=horario.pelicula.pk)
    else:
        form = HorarioForm(instance=horario)

    return render(request, 'horarios/crear_horario.html', {'form': form, 'horario': horario})

def eliminar_horario(request, horario_id):
    horario = get_object_or_404(Horario, id=horario_id)

    if request.method == 'POST':
        horario.delete()
        return redirect('cineapp:lista_horarios_pelicula', pelicula_id=horario.pelicula.pk)

    return render(request, 'horarios/eliminar_horario.html', {'horario': horario})


class AsientoList(View):
    def get(self, request, pelicula_id):
        pelicula = get_object_or_404(Pelicula, id=pelicula_id)
        asientos = Asiento.objects.filter(pelicula=pelicula)
        return render(request, 'asientos/asiento_list.html', {'pelicula': pelicula, 'asientos': asientos})

class AsientoCreate(View):

    def get(self, request, pelicula_id):
        pelicula = get_object_or_404(Pelicula, id=pelicula_id)
        form = AsientoForm()  #Instancia del form vacio
        return render(request, 'asientos/asiento_form.html', {'pelicula': pelicula, 'form': form})

    def post(self, request, pelicula_id):
        pelicula = get_object_or_404(Pelicula, id=pelicula_id)
        form = AsientoForm(request.POST)

        if form.is_valid():
            numero_asiento = form.cleaned_data['numero_asiento']
            disponible = form.cleaned_data['disponible']
            Asiento.objects.create(pelicula=pelicula, numero_asiento=numero_asiento, disponible=disponible)
            return redirect('cineapp:asiento_list', pelicula_id=pelicula.id)

        return render(request, 'asientos/asiento_form.html', {'pelicula': pelicula, 'form': form})

class AsientoUpdate(View):
    def get(self, request, pelicula_id, asiento_id):
        asiento = get_object_or_404(Asiento, id=asiento_id)
        form = AsientoForm(instance=asiento)
        return render(request, 'asientos/asiento_form.html', {'asiento': asiento, 'form': form})

    def post(self, request, pelicula_id, asiento_id):
        asiento = get_object_or_404(Asiento, id=asiento_id)
        form = AsientoForm(request.POST, instance=asiento)

        if form.is_valid():
            form.save()
            return redirect('cineapp:asiento_list', pelicula_id=pelicula_id)

        return render(request, 'asientos/asiento_form.html', {'asiento': asiento, 'form': form})

class AsientoDelete(DeleteView):
    model = Asiento
    template_name = 'asientos/asiento_confirm_delete.html'
    
    def get_success_url(self):
        pelicula_id = self.kwargs['pelicula_id']
        return reverse('cineapp:asiento_list', kwargs={'pelicula_id': pelicula_id})
    