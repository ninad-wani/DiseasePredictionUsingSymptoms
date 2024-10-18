package com.shrinathit.chatbot;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.Toast;

public class SearchActivity extends AppCompatActivity {
    WebView webView;
    String query;
    EditText searchET;
    ImageView searchBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search);
        webView = (WebView)findViewById(R.id.webView);
        searchET = findViewById(R.id.searchET);
        searchBtn = findViewById(R.id.searchBtn);
        searchBtn.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                query = searchET.getText().toString();
                if(query.length() == 0){
                    Toast.makeText(SearchActivity.this,"Please enter a disease to get info",Toast.LENGTH_SHORT).show();
                    //finish();
                }
                else {
                    webView.setWebViewClient(new WebViewClient());
                    webView.loadUrl("https://www.google.com/search?q=" + query);
                }
            }
        });

    }
}