package com.shrinathit.chatbot;

import androidx.annotation.MainThread;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

public class LoginActivity extends AppCompatActivity {
    EditText ETEmail, ETPass;
    Button loginBtn;
    TextView regText;
    ProgressBar progressBar;
    FirebaseAuth fAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        ETEmail = findViewById(R.id.ETEmail);
        ETPass = findViewById(R.id.ETPass);
        progressBar = findViewById(R.id.progressBar);
        fAuth = FirebaseAuth.getInstance();
        //Intent i = new Intent(this,MainActivity.class);
        regText = (TextView)findViewById(R.id.regText);
        loginBtn =(Button)findViewById(R.id.loginBtn);
        loginBtn.setBackgroundColor(Color.parseColor("#FFC107"));
        if(fAuth.getCurrentUser() != null){
            startActivity(new Intent(getApplicationContext(),MainActivity.class));
        }
        loginBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                regText.setVisibility(View.INVISIBLE);
                String email = ETEmail.getText().toString().trim();
                String pass = ETPass.getText().toString().trim();
                if(TextUtils.isEmpty(email)){
                    ETEmail.setError("Email is required!");
                    return;
                }
                if(TextUtils.isEmpty(pass)){
                    ETPass.setError("Password is required!");
                }
                if(pass.length() < 6){
                    ETPass.setError("Password must be atleast 6 characters!");
                }
                progressBar.setVisibility(View.VISIBLE);

                fAuth.signInWithEmailAndPassword(email,pass).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        if(task.isSuccessful()){
                            Toast.makeText(LoginActivity.this,"Login Success",Toast.LENGTH_SHORT).show();
                            startActivity(new Intent(getApplicationContext(),MainActivity.class));
                        }else{
                            regText.setVisibility(View.VISIBLE);
                            progressBar.setVisibility(View.INVISIBLE);
                            Toast.makeText(LoginActivity.this,"Error : "+task.getException().getMessage(),Toast.LENGTH_SHORT).show();
                        }
                    }
                });
            }
        });
        Intent j = new Intent(this,RegisterActivity.class);

        regText.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(j);
            }
        });
    }

}