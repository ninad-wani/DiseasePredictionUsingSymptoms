package com.shrinathit.chatbot;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class ReceiveAdapter extends RecyclerView.Adapter<ReceiveAdapter.ViewHolder>{
    Context context;
    String[] symptoms;


    public static class ViewHolder extends RecyclerView.ViewHolder{
        TextView rowName;
        TextView sent_time;
        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            rowName = itemView.findViewById(R.id.msg);
            sent_time = itemView.findViewById(R.id.text_message_time);
        }
    }

    public ReceiveAdapter(Context context,String[] symptoms){
        this.context = context;
        this.symptoms = symptoms;
    }

    @NonNull
    @Override
    public ReceiveAdapter.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(context);
        View view = inflater.inflate(R.layout.message_received,parent,false);
        ViewHolder viewHolder = new ViewHolder(view);
        return viewHolder;
    }

    @Override
    public void onBindViewHolder(@NonNull ReceiveAdapter.ViewHolder holder, int position) {
        holder.rowName.setText(symptoms[position]);
        String currentsTime = new SimpleDateFormat("HH:mm:ss", Locale.getDefault()).format(new Date());
        holder.sent_time.setText(currentsTime.toString());
    }

    @Override
    public int getItemCount() {
        return symptoms.length;
    }
}