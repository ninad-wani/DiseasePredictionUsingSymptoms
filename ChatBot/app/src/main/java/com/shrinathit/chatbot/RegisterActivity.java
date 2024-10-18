package com.shrinathit.chatbot;

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
import com.google.firebase.auth.UserProfileChangeRequest;

public class RegisterActivity extends AppCompatActivity {
    EditText ETfullName,ETEmail,ETPass,ETPhone;
    FirebaseAuth fAuth;
    ProgressBar progressBar;
    Button regBtn;
    TextView loginText;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        ETfullName = findViewById(R.id.ETfullName);
        ETEmail = findViewById(R.id.ETEmail);
        ETPass = findViewById(R.id.ETPass);
        ETPhone = findViewById(R.id.ETPhone);
        fAuth = FirebaseAuth.getInstance();
        progressBar = findViewById(R.id.progressBar);
        loginText = (TextView)findViewById(R.id.loginText);

        if(fAuth.getCurrentUser() != null){
            startActivity(new Intent(getApplicationContext(),MainActivity.class));
        }

        Intent i = new Intent(this,MainActivity.class);
        regBtn = (Button)findViewById(R.id.regBtn);
        regBtn.setBackgroundColor(Color.parseColor("#FFC107"));
        regBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                loginText.setVisibility(View.INVISIBLE);
                String email = ETEmail.getText().toString().trim();
                String pass = ETPass.getText().toString().trim();
                if(TextUtils.isEmpty(email)) {
                    ETEmail.setError("Email is required!");
                    return;
                }
                if(TextUtils.isEmpty(pass)){
                    ETPass.setError("Password is required!");
                    return;
                }
                if(pass.length() < 6){
                    ETPass.setError("Password must be atleast 6 characters!");
                    return;
                }
                progressBar.setVisibility(View.VISIBLE);

                //Register user in firebase

                fAuth.createUserWithEmailAndPassword(email,pass).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        if(task.isSuccessful()){
                            Toast.makeText(RegisterActivity.this,"Registration Success",Toast.LENGTH_SHORT).show();
                            startActivity(i);
                        }else{
                            loginText.setVisibility(View.VISIBLE);
                            progressBar.setVisibility(View.INVISIBLE);
                            Toast.makeText(RegisterActivity.this,"Error : "+task.getException().getMessage(),Toast.LENGTH_SHORT).show();
                        }
                    }
                });


            }
        });
        Intent j = new Intent(this,LoginActivity.class);

        loginText.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(j);
            }
        });
    }
}