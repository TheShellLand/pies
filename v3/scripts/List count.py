import pip

distribution = pip.get_installed_distributions()
size = len(distribution)

print('Number of packages installed:', size)