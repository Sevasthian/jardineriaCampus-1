from tabulate import tabulate
import modules.getClients as cliente
import modules.getOficina as oficina

print(tabulate(oficina.getAllCiudadTelefono("España"), tablefmt="grid"))

