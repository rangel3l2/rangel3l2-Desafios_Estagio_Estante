import {  NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DefaultComponent } from './core/layout/default/default.component';
import { WebscrapingManagerComponent } from './core/components/webscraping-manager/webscraping-manager.component';

const routes: Routes = [
  {
    path:'',
    component:DefaultComponent,
    children:[
      {
        path:'',
        component: WebscrapingManagerComponent

      }
    ] 
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
