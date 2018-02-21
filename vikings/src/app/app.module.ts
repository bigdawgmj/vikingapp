import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { TableModule } from 'primeng/table';
import { MatTabsModule } from '@angular/material/tabs';
import { MatTableModule } from '@angular/material/table';
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';

import { AppComponent } from './app.component';
import { TeamComponent } from './vsts/components/team/team.component';
import { TestService } from './vsts/services/test.service';
import { HttpClientModule } from '@angular/common/http';
import { WitComponent } from './vsts/components/wit/wit.component';

@NgModule({
  declarations: [
    AppComponent,
    TeamComponent,
    WitComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpClientModule,
    MatTabsModule,
    MatCardModule,
    MatInputModule,
    MatButtonModule,
    MatTableModule,
    TableModule
  ],
  providers: [TestService],
  bootstrap: [AppComponent]
})
export class AppModule { }
