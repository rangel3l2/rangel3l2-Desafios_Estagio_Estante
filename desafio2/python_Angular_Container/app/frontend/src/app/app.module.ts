import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HeaderComponent } from './core/components/header/header.component';
import { FooterComponent } from './core/components/footer/footer.component';
import { DefaultComponent } from './core/layout/default/default.component';
import { DefaultModule } from './core/layout/default/default.module';
import { ServicesModule } from './core/services/services.module';

@NgModule({
  declarations: [
    AppComponent,
  
  ],
  imports: [
    ServicesModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    DefaultModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
