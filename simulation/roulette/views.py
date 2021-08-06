from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .utils import Player
import matplotlib.pyplot as plt
from .forms import GraphForm
from .models import Graph
import secrets
import mimetypes


def home_view(request):
	graph_form=GraphForm()
	if request.method == "POST":
		graph_form = GraphForm(request.POST)
		if graph_form.is_valid():
			graph=graph_form.save()
			
			player_1=Player(graph.turns, graph.money, graph.bet, 'Henry')
			player_2=Player(graph.turns, graph.money, graph.bet, 'Bob')
			player_3=Player(graph.turns, graph.money, graph.bet, 'Silvie')
			player_4=Player(graph.turns, graph.money, graph.bet, 'John')
			player_5=Player(graph.turns, graph.money, graph.bet, 'Alfie')
			players=[player_1, player_2, player_3, player_4, player_5]

			for player in players:
				player.create_turns()
				player.play()
				money_list=[]
				turns_list=[]
				for key, value in player.data_dict.items():
					turns_list.append(key)
					money_list.append(value)
				plt.plot(turns_list, money_list, label=player.__str__())

			plt.xlabel('Turns')
			plt.ylabel('Money')
			plt.title('Outcome of 5 players after playing {} turns'.format(graph.turns))
			plt.legend()
			fig_name=secrets.token_hex(nbytes=16)
			plt.savefig('media/graphs/g{}.png'.format(fig_name))

			graph.graph='graphs/g{}.png'.format(fig_name)
			graph_form.save()

			return redirect('result', graph.graph_id)
	content={
		'graph_form':graph_form,
	}
	return render(request, 'home.html', content)


def result_view(request, pk):
	graph=get_object_or_404(Graph, graph_id=pk)
	print(graph)

	if request.method == "POST":
		with open(graph.graph.path, 'rb') as f:
			mime_type, _ = mimetypes.guess_type(graph.graph.path)
			response = HttpResponse(f, content_type=mime_type)
			graphname="{}".format(graph.graph)
			graphname=graphname[7:]
			response['Content-Disposition'] = "attachment; filename={}".format(graphname)
			return response
	content={
		'graph': graph,
	}
	return render(request, 'result.html', content)


def view_404(request, exception=None):
    return redirect('home')