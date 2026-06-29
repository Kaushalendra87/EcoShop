from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.http import HttpResponse
from django.utils.encoding import force_bytes,force_str
from .forms import CreateUserForm, ProfileForm
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)

            #Email Verification Code
            subject = "Verify your email to activate your account"
            message =render_to_string('users/email-verification.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })

            try:
                user.email_user(subject=subject, message=message)
            except Exception as e:
                import sys
                print(f"ERROR sending verification email: {e}", file=sys.stderr)
                # Print verification URL directly to stdout/stderr in dev so developers can copy/paste
                verification_url = f"http://{current_site.domain}/users/email-verification/{urlsafe_base64_encode(force_bytes(user.pk))}/{account_activation_token.make_token(user)}/"
                print(f"\n--- VERIFICATION LINK (DEVELOPMENT) ---\n{verification_url}\n---------------------------------------\n", file=sys.stdout)

            return redirect ('email-verification-sent')
        
    return render(request,'users/register.html', {'form':form})


@login_required
def profile(request):
    form = ProfileForm(instance=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')

    return render(request, 'users/profile.html', {'form': form})

def email_verification(request,uidb64,token):
    try:
        unique_id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=unique_id)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('email-verification-success')
    else:
        return redirect('email-verification-failed')



def email_verification_sent(request):
    return render(request, 'users/email-verification-sent.html')

def email_verification_success(request):
    return render(request,'users/email-verification-success.html')

def email_verification_failed(request):
    return render(request,'users/email-verification-failed.html')

