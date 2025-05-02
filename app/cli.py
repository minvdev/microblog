import os
import click
from flask import Blueprint
from app import models
from app.models import SearchableMixin

bp = Blueprint('cli', __name__, cli_group=None)

@bp.cli.group()
def translate():
    """Translation and localization commands."""
    pass

@translate.command()
@click.argument('lang')
def init(lang):
    """Initialize a new language."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system(
        'pybabel init -i messages.pot -d app/translations -l ' + lang):
        raise RuntimeError('init command failed')
    os.remove('messages.pot')

@translate.command()
def update():
    """Update all languages."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel update -i messages.pot -d app/translations'):
        raise RuntimeError('update command failed')
    os.remove('messages.pot')
    
@translate.command()
def compile():
    """Compile all languages."""
    if os.system('pybabel compile -d app/translations'):
        raise RuntimeError('compile command failed')


@bp.cli.group()
def searching():
    """Search functionality mantenance commands."""
    pass

@searching.command()
@click.argument('model')
def reindex(model):
    """Refresh an index with all the data from the relational side to the elastic side."""
    ModelClass = getattr(models, model)
    
    if ModelClass is None:
        raise RuntimeError(f'reindex command failed, Model str[{model}] cls[{ModelClass}] does not exist.')
        
    if not issubclass(ModelClass, SearchableMixin):
        raise RuntimeError(f'reindex command failed, Model str[{model}] cls[{ModelClass}] is not a searcheable (does not inherit from SearcheableMixin Class)')
    
    ModelClass.reindex()
    click.echo(f'Reindexed {ModelClass}.')
