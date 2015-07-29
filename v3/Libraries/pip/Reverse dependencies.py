import pip

package_name = 'pymongo'
rev_dep = [
    pkg.project_name for pkg in pip.get_installed_distributions() if
    package_name in [requirement.project_name for requirement in pkg.requires()]
    ]