from app import create_app
from rq import get_current_job
from app import db
from app.models import Task

app = create_app()
app.app_context().push()

def _set_task_progress(progress):
    job = get_current_job()
    if job:
        job.meta['progress'] = progress
        job.save_meta()
        task = db.session.get(Task, job.get_id())
        task.user.add_notification('task_progress', {'task_id': job.get_id(),
                                                     'progress': progress})
        if progress >= 100:
            task.complete = True
        db.session.commit()

def export_posts(user_id):
    try:
        # read user posts from db
        # send email with data to user
        pass
    except Exception:
        # handle unexpected errors
        pass
    finally:
        # handle clean up
        pass
