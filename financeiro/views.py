from django.shortcuts import render,redirect
from . models import Usuario, Despesas
from .forms import UsuarioForm , DespesasForm
# Create your views here.

def home(request):
    return render (request, 'home.html', {})

def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render (request, 'usuarios/list.html', {'usuarios': usuarios})

def usuario_show(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    return render(request, 'usuarios/show.html', {'usuario': usuario})

def despesa_list (request):
    despesas = Despesas.objects.all()
    return render(request, 'despesas/list.html', {'despesas': despesas}) 

def despesa_show(request, despesa_id):
    despesa = Despesas.objects.get(pk=despesa_id)
    return render(request, 'despesas/show.html', {'despesa': despesa})

def usuario_form (request):
    if(request.method == 'POST'):
        form = UsuarioForm(request.POST)
        form.save()

        return redirect('/financeiro/usuarios/')
    else:    
        form = UsuarioForm()
        return render (request, 'usuarios/form.html',{'form':form})

def despesa_form (request):
    if(request.method == 'POST'):
        form = DespesasForm(request.POST)
        form.save()

        return redirect('/financeiro/despesas/')
    else:    
        form = DespesasForm()
        return render (request, 'despesas/form.html',{'form':form})

def usuario_edit (request, usuario_id):
    if (request.method == 'POST'):
        usuario = Usuario.objects.get(pk=usuario_id)
        form = UsuarioForm(request.POST, instance = usuario)
        if (form.is_valid):
            form.save()
            return redirect ('/financeiro/usuarios/')
        else:
            return render(request, 'usuarios/edit.html', {'form':form, 'usuario_id':usuario_id})
    else:
        usuario = Usuario.objects.get(pk=usuario_id)
        form = UsuarioForm(instance = usuario)
        return render (request, 'usuarios/edit.html',{'form':form, 'usuario_id':usuario_id})

def despesa_edit (request, despesa_id):
    if (request.method == 'POST'):
        despesa = Despesas.objects.get(pk=despesa_id)
        form = DespesasForm(request.POST, instance = despesa)
        if (form.is_valid):
            form.save()
            return redirect ('/financeiro/despesas/')
        else:
            return render(request, 'despesas/edit.html', {'form':form, 'despesa_id':despesa_id})
    else:
        despesa = Despesas.objects.get(pk=despesa_id)
        form = DespesasForm(instance = despesa)
        return render (request, 'despesas/edit.html',{'form':form, 'despesa_id':despesa_id})