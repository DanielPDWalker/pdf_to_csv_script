
"""CLI entrypoint 'notebook' command"""

import click


@click.group()
@click.pass_context
def pdf_to_csv(ctx, **kwargs):
    """CLI entrypoint and base command"""

    ctx.ensure_object(dict)
    ctx.obj.update(kwargs)